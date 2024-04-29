from app.models import BookingModel
from .base_service import BaseService
from app.constants import payment_methods
from app.constants import service_statuses
from app.constants import payment_statuses
from datetime import datetime, timedelta
from collections import defaultdict


class BookingService(BaseService):
    def __init__(self) -> None:
        super().__init__(BookingModel)


    def add_service_status_with_this(self, items):
        for item in items["data"]:
            item['service_statuses'] = []

            status_value = service_statuses.get_value(item["service_status"])
            item['service_status_name']=status_value

            item['service_statuses'].append(status_value)
            item['service_statuses'].extend(item for item in service_statuses.get_all_values() if item != status_value)
            item['service_statuses'] = list(item['service_statuses'])
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

    def get_bookings_by_user_id(self,user_id,request,columns):
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

    def get_booking_statuses_count(self,time_range):
        status_mapping=service_statuses.get_all_items_as_dict()
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

        orders_query = BookingModel.query

        if start_date is not None:
            orders_query = orders_query.filter(BookingModel.created_at >= start_date)
        orders_query = orders_query.filter(BookingModel.created_at <= end_date, BookingModel.is_active == True)

        services = orders_query.all()

        status_counts = defaultdict(int)
        for service in services:
            status_name = status_mapping.get(service.service_status)
            if status_name:
                status_counts[status_name] += 1

        present_statuses = [status_name for status_name in status_mapping.values() if status_counts[status_name] > 0]
        status_counts_list = []
        for status_name in present_statuses:
            status_counts_list.append(status_counts[status_name])

        return {
            "service_statuses": present_statuses,
            "status_counts": status_counts_list
        }