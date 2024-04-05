from db import db
from app.models import ServiceTypeModel
from .base_service import BaseService


class ServiceTypeService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceTypeModel)
