from app.models import OrderModel
from .base_service import BaseService
from app.constants import payment_methods
from app.constants import order_statuses
from app.constants import payment_statuses
from app.models import ProductModel
from collections import Counter
from datetime import datetime, timedelta
from collections import defaultdict
from sqlalchemy import func

class OrderService(BaseService):
    def __init__(self) -> None:
        super().__init__(OrderModel)


    def add_order_status_with_this(self, items):
        for item in items["data"]:
            item['order_statuses'] = []

            status_value = order_statuses.get_value(item["order_status"])
            item['order_status_name']=status_value

            item['order_statuses'].append(status_value)
            item['order_statuses'].extend(item for item in order_statuses.get_all_values() if item != status_value)
            item['order_statuses'] = list(item['order_statuses'])
        return items

    def add_payment_status_with_this(self, items):
        for item in items["data"]:
            item['payment_statuses'] = []

            status_value = payment_statuses.get_value(item["payment_status"])
            item['payment_status_name']=status_value

            item['payment_statuses'].append(status_value)
            item['payment_statuses'].extend(item for item in payment_statuses.get_all_values() if item != status_value)
            item['payment_statuses'] = list(item['payment_statuses'])
        return items


    def add_payment_method_with_this(self, items):
        for item in items["data"]:
            item['payment_method_name']=payment_methods.get_value(item["payment_method"])
        return items
    
    def add_payment_status_name_with_this(self,orders):
        for order in orders['data']:
            order['payment_status_name']=payment_statuses.get_value(order["payment_status"])
        return orders

    def get_orders_by_user_id(self,user_id,request,columns):
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        query = self.model.query
        query = query.filter(self.model.user_id == user_id)
        # Perform pagination after filtering
        paginated_query = query.paginate(page=page, per_page=page_size, error_out=False)
        paginated_data = paginated_query.items

        # Format data
        formatted_data = [{key: getattr(item, key) for key in columns} for item in paginated_data]

        return {
            "recordsTotal": paginated_query.total,
            "recordsFiltered": len(paginated_data),
            "data": formatted_data,
            "page": page,
            "total_pages": paginated_query.pages
        }

    def get_top_10_ordered_products(self):
        all_orders = self.model.query.all()

        product_counts = Counter(order.product_id for order in all_orders)
        top_10_product_ids = [product_id for product_id, _ in product_counts.most_common(10)]


        top_10_products = []
        for product_id in top_10_product_ids[:10]:
            product = ProductModel.query.get(product_id)
            if product:
               top_10_products.append(product)

        return top_10_products

    def get_ordered_data_for_Chart(self, time_range):
        dates = []
        counts = []
        if time_range == 'Weekly':
            end_date = datetime.now()
            # start_date = end_date - timedelta(days=6)
            start_date = end_date - timedelta(days=end_date.weekday())
            current_date = start_date
            while current_date <= end_date:
                day_start = datetime.combine(current_date, datetime.min.time())
                day_end = datetime.combine(current_date, datetime.max.time())

                order_count = (
                    OrderModel.query
                    .filter(OrderModel.created_at >= day_start)
                    .filter(OrderModel.created_at <= day_end)
                    .filter(OrderModel.is_active ==True)
                    .count()
                )

                dates.append(current_date.strftime('%Y-%m-%d'))
                counts.append(order_count)
                current_date += timedelta(days=1)

        elif time_range == 'Yearly':
            current_year = datetime.now().year
            current_month = datetime.now().month
            start_date = datetime(current_year, 1, 1)
            next_month_start = datetime(current_year, current_month + 1, 1)
            end_date = next_month_start - timedelta(days=1)
            order_count = OrderModel.query.filter(
                OrderModel.created_at >= start_date,
                OrderModel.created_at <= end_date,
                OrderModel.is_active ==True
            ).all()
            monthly_counts = defaultdict(int)
            for order in order_count:
                month_key = (order.created_at.year, order.created_at.month)
                monthly_counts[month_key] += 1

            for month in range(1, current_month + 1):
                first_day_of_month = datetime(current_year, month, 1)
                month_count = monthly_counts[(current_year, month)]
                date_range = f"{first_day_of_month.strftime('%B')}"
                dates.append(date_range)
                counts.append(month_count)

        elif time_range == 'Monthly':
            end_date = datetime.now()
            start_date = end_date - timedelta(days=29)


            current_date = start_date
            while current_date <= end_date:
                week_start = current_date
                week_end = min(current_date + timedelta(days=6), end_date)
                order_count = (
                    OrderModel.query
                    .filter(OrderModel.created_at >= week_start)
                    .filter(OrderModel.created_at <= week_end + timedelta(days=1))
                    .filter(OrderModel.is_active ==True)
                    .count()
                )

                dates.append(f"{week_start.strftime('%d/%m')} - {week_end.strftime('%d/%m')}")
                counts.append(order_count)

                current_date += timedelta(days=6)

        elif time_range == 'Overall':
            min_date = OrderModel.query.with_entities(func.min(OrderModel.created_at)).scalar()
            max_date = OrderModel.query.with_entities(func.max(OrderModel.created_at)).scalar()
            start_year = min_date.year if min_date else datetime.now().year
            end_year = max_date.year if max_date else datetime.now().year

            yearly_counts = defaultdict(int)
            for year in range(start_year, end_year + 1):
                orders = OrderModel.query.filter(
                    func.extract('year', OrderModel.created_at) == year,
                    OrderModel.is_active == True
                ).all()
                yearly_counts[year] = len(orders)
            for year in range(start_year, end_year + 1):
                dates.append(str(year))
                counts.append(yearly_counts[year])

        dataset = {
            "label": dates,
            "data": counts
        }

        return dataset

    def get_order_statuses_count(self,time_range):

        status_mapping=order_statuses.get_all_items_as_dict()
        end_date = datetime.now()
        if time_range == 'Weekly':
            start_date = end_date - timedelta(days=end_date.weekday())
        elif time_range == 'Monthly':
            start_date = end_date.replace(day=1)- timedelta(days=1)
        elif time_range == 'Yearly':
            start_date = end_date.replace(month=1, day=1)
        elif time_range == 'Overall':
            start_date = None
            end_date = datetime.now()

        orders_query = OrderModel.query
        if start_date is not None:
            orders_query = orders_query.filter(OrderModel.created_at >= start_date)
        orders_query = orders_query.filter(OrderModel.created_at <= end_date, OrderModel.is_active == True)

        orders = orders_query.all()

        status_counts = defaultdict(int)
        for order in orders:
            status_name = status_mapping.get(order.order_status)
            if status_name:
                status_counts[status_name] += 1
        present_statuses = [status_name for status_name in status_mapping.values() if status_counts[status_name] > 0]
        status_counts_list = [status_counts[status_name] for status_name in present_statuses]

        return {
            "order_statuses": present_statuses,
            "status_counts": status_counts_list
        }

    def get_all_orders(self,time_range):
        end_date = datetime.now()
        if time_range == 'Weekly':
            start_date = end_date - timedelta(days=end_date.weekday())
        elif time_range == 'Monthly':
            start_date = end_date.replace(day=1)- timedelta(days=1)
        elif time_range == 'Yearly':
            start_date = end_date.replace(month=1, day=1)
        elif time_range == 'Overall':
            start_date = None

        if start_date is not None:
               total_orders = OrderModel.query.filter(
                   OrderModel.created_at >= start_date,
                   OrderModel.created_at <= end_date,
                   OrderModel.is_active == True
               ).count()
        else:
            total_orders = OrderModel.query.filter(
                OrderModel.is_active == True
            ).count()
        total_orders = OrderModel.query.filter(
            OrderModel.created_at >= start_date,
            OrderModel.created_at <= end_date,
            OrderModel.is_active==True
        ).count()

        return total_orders



    def get_by_user_and_product_id(self, product_id, user_id):
        orders = self.model.query.filter_by(product_id=product_id, user_id=user_id).all()
        
        for order in orders:
            if order.product_id == product_id and order.user_id == user_id:
                return order
        return None


    

