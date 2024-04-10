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
