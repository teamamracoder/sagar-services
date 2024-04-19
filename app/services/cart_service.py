from app.models import CartModel, ProductModel
from .base_service import BaseService
from app.constants import cart_statuses


class CartService(BaseService):
    def __init__(self) -> None:
        super().__init__(CartModel)
        self.product_model=ProductModel()

    def add_status_with_cart(self, carts):
        for cart in carts["data"]:
            cart['statuses'] = []
            status_value = cart_statuses.get_value(cart["status"])
            cart['status_name']=status_value

            cart['statuses'].append(status_value)
            cart['statuses'].extend(item for item in cart_statuses.get_all_values() if item != status_value)
            cart['statuses'] = list(cart['statuses'])
        return carts

    def get_cart_items_by_user_id(self,user_id):
        try:
            # Query the database to get cart items for the given user id
            cart_items = self.model.query.filter_by(user_id=user_id, is_active=True).all()

            # Return list of cart items
            return cart_items

        except Exception as e:
            raise ValueError(str(e))  # Raise an exception if an error occurs
        

    def get_cart_item_by_user_id_product_id(self,user_id,product_id):
        try:
            # Query the database to get cart items for the given user id
            cart_item = self.model.query.filter_by(user_id=user_id, product_id=product_id).first()

            # Return list of cart items
            return cart_item

        except Exception as e:
            raise ValueError(str(e))  # Raise an exception if an error occurs