from app.models import BookingModel
from .base_service import BaseService
from app.constants import payment_methods
from app.constants import service_statuses
from app.constants import payment_statuses


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
