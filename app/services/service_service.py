from db import db
from app.models import ServiceModel
from .base_service import BaseService


class ServiceService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceModel)



