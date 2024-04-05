from app.models import WishlistModel
from .base_service import BaseService


class WishlistService(BaseService):
    def __init__(self) -> None:
        super().__init__(WishlistModel)

