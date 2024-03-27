from db import db
from app.models import ServiceModel


class ServiceService:
    def create(self, **kwargs):
        service = ServiceModel(**kwargs)
        db.session.add(service)
        db.session.commit()
        return service


    def get(self):
        return ServiceModel.query.all()

    def get_by_id(self, id):
        return ServiceModel.query.get(id)

    def update(self, id, **kwargs):
        service = self.get_by_id(id)
        if service:
            for key, value in kwargs.items():
                setattr(service, key, value)
            db.session.commit()
            return service
        return None

    def status(self,id):
        service = ServiceModel.query.get(id)
        if not service.is_active:
            service.is_active = True
        else:
            service.is_active = False
        db.session.commit()
        return service.is_active