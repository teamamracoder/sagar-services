from db import db
from app.models import ServiceTypeModel


class ServiceTypeService:
    def create(self,**kwargs):
        service_type = ServiceTypeModel(**kwargs)
        db.session.add(service_type)
        db.session.commit()
        return service_type

    def get(self):
        return ServiceTypeModel.query.all()

    def get_by_id(self, id):
        return ServiceTypeModel.query.get(id)

    def update(self, id, **kwargs):
        service_type = self.get_by_id(id)
        if service_type:
            for key, value in kwargs.items():
                setattr(service_type, key, value)
            db.session.commit()
            return service_type
        return None

    def status(self,id):
        service_type = ServiceTypeModel.query.get(id)
        if not service_type.is_active:
            service_type.is_active = True
        else:
            service_type.is_active = False
        db.session.commit()
        return service_type.is_active