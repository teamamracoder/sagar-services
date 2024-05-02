from app.models import CartModel, ProductModel
from .base_service import BaseService
from app.constants import cart_statuses
from db import db


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
            cart_item=self.model.query.filter_by(user_id=user_id, product_id=product_id).first()
            return cart_item
        except Exception as e:
            return None

    def get_active_cart_item_by_user_id_product_id(self,user_id,product_id):
        return self.model.query.filter_by(user_id=user_id, product_id=product_id, is_active=True).first()

    def serialize_cart_item(self, cart_item):
        if cart_item:
            serialized_cart_item = {key: getattr(cart_item, key) for key in cart_item.__dict__.keys() if not key.startswith("_")}
            return serialized_cart_item
        else:
            return None

    def add_cart_with_user_and_product(self, user_id, datas):
        try:
            user_id=user_id
            for data in datas["data"]:
                cart_item = self.get_active_cart_item_by_user_id_product_id(user_id, data["id"])
                serialized_cart_item = self.serialize_cart_item(cart_item)
                data["cart"] = serialized_cart_item
            return datas
        except Exception as e:
            return datas
  
    def update_cart_status(self, user_id, product_id, cart_status):
        cart_item = self.model.query.filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.cart_status = cart_status
            self.status(cart_item.id)
            db.session.commit()
        return True

    def get_total_cart_items_by_user_id(self,user_id):
            cart_items = self.model.query.filter_by(user_id=user_id, is_active=True).count()
            return cart_items

