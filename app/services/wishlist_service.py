from app.models import WishlistModel
from .base_service import BaseService


class WishlistService(BaseService):
    def __init__(self) -> None:
        super().__init__(WishlistModel)


    def get_wishlist_items_by_user_id(self,user_id):
        try:
            # Query the database to get wishlist items for the given user id
            return self.model.query.filter_by(user_id=user_id, is_active=True).all()

        except Exception as e:
            raise ValueError(str(e))  # Raise an exception if an error occurs

    def get_wishlist_item_by_user_id_product_id(self,user_id,product_id):
        return self.model.query.filter_by(user_id=user_id, product_id=product_id).first()

    def get_active_wishlist_item_by_user_id_product_id(self,user_id,product_id):
        return self.model.query.filter_by(user_id=user_id, product_id=product_id, is_active=True).first()

    def serialize_wishlist_item(self, wishlist_item):
        if wishlist_item:
            serialized_wishlist_item = {key: getattr(wishlist_item, key) for key in wishlist_item.__dict__.keys() if not key.startswith("_")}
            return serialized_wishlist_item
        else:
            return None

    def add_wishlist_with_user_and_product(self, user_id, datas):
        if user_id:
            for data in datas["data"]:
                wishlist_item = self.get_active_wishlist_item_by_user_id_product_id(user_id, data["id"])
                serialized_wishlist_item = self.serialize_wishlist_item(wishlist_item)
                data["wishlist"] = serialized_wishlist_item
            return datas
        return datas

    def get_total_wishlist_items_by_user_id(self,user_id):
            cart_items = self.model.query.filter_by(user_id=user_id, is_active=True).count()
            return cart_items

