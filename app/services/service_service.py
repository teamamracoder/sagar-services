from app.models import ServiceModel
from .base_service import BaseService

class ServiceService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceModel)

    def add_service_with_this(self, datas):
        for data in datas["data"]:
            service_name = self.get_service_by_id(data["service_id"])
            if service_name:
                data["service_name"] = service_name
            else:
                # Handle case where service with the given ID doesn't exist
                data["service_name"] = "Unknown"
        return datas

    def get_service_by_id(self, id):
        service = ServiceModel.query.filter_by(id=id).first()
        if service:
            return service.service_name
        else:
            return None  # or raise an exception depending on your use case
