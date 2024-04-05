from app.models import CartModel
from .base_service import BaseService
from app.constants import cart_statuses


class CartService(BaseService):
    def __init__(self) -> None:
        super().__init__(CartModel)

    def add_status_with_cart(self, carts):
        for cart in carts["data"]:
            cart['statuses'] = []
            status_value = cart_statuses.get_value(cart["status"])
            cart['status_name']=status_value

            cart['statuses'].append(status_value)
            cart['statuses'].extend(item for item in cart_statuses.get_all_values() if item != status_value)
            cart['statuses'] = list(cart['statuses'])
        return carts
