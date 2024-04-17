from app.models import WishlistModel
from .base_service import BaseService


class WishlistService(BaseService):
    def __init__(self) -> None:
        super().__init__(WishlistModel)


    def get_wishlist_items_by_user_id(self,user_id):
        try:
            # Query the database to get wishlist items for the given user id
            wishlist_items = self.model.query.filter_by(user_id=user_id, is_active=True).all()

            # Return list of wishlist items
            return wishlist_items

        except Exception as e:
            raise ValueError(str(e))  # Raise an exception if an error occurs