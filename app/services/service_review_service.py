from app.models import ServiceReviewModel
from .base_service import BaseService


class ServiceReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceReviewModel)