from db import db
from app.models import ServiceTypeModel
from .base_service import BaseService


class ServiceTypeService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceTypeModel)
     
    def get_active(self):
        return ServiceTypeModel.query.filter_by(is_active=True).order_by(ServiceTypeModel.type_name).all()

    def add_service_type_with_services(self, services: list) -> list:
        for service in services["data"]:
            service["type_name"] = self.get_service_name_by_id(service["service_type_id"])
        return services

    def get_service_name_by_id(self,service_type_id):
        return ServiceTypeModel.query.filter_by(id=service_type_id).first().type_name
    
