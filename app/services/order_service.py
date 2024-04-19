from app.models import OrderModel
from .base_service import BaseService
from app.constants import payment_methods
from app.constants import order_statuses
from app.constants import payment_statuses
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