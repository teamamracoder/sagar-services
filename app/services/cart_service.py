from app import db
from app.models import CartModel
from .base_service import BaseService
from app.constants import cart_status


class CartService(BaseService):
    def __init__(self) -> None:
        super().__init__(CartModel)

    def add_status_with_cart(self, carts):
        for cart in carts["data"]:
            cart["status_name"] = cart_status.get_value(cart["status"])
        return carts
