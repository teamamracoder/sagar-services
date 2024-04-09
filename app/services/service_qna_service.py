from app.models import ServiceQnAModel
from .base_service import BaseService


class ServiceQnAService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceQnAModel)