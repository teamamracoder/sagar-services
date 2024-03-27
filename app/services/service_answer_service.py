from db import db
from app.models import ServiceAnswerModel


class ServiceAnswerService:
    def create(self,**kwargs):
        service_answer = ServiceAnswerModel(**kwargs)
        db.session.add(service_answer)
        db.session.commit()
        return service_answer

    def get(self):
        return ServiceAnswerModel.query.all()

    def get_by_id(self, id):
        return ServiceAnswerModel.query.get(id)

    def update(self, id, **kwargs):
        service_answer = self.get_by_id(id)
        if service_answer:
            for key, value in kwargs.items():
                setattr(service_answer, key, value)
            db.session.commit()
            return service_answer
        return None

    def status(self,id):
        service_answer = ServiceAnswerModel.query.get(id)
        if not service_answer.is_active:
            service_answer.is_active = True
        else:
            service_answer.is_active = False
        db.session.commit()
        return service_answer.is_active