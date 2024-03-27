from db import db
from app.models import ServiceQuestionModel


class ServiceQuestionService:
    def create(self,**kwargs):
        service_question = ServiceQuestionModel(**kwargs)
        db.session.add(service_question)
        db.session.commit()
        return service_question

    def get(self):
        return ServiceQuestionModel.query.all()

    def get_by_id(self, id):
        return ServiceQuestionModel.query.get(id)

    def update(self, id, **kwargs):
        service_question = self.get_by_id(id)
        if service_question:
            for key, value in kwargs.items():
                setattr(service_question, key, value)
            db.session.commit()
            return service_question
        return None

    def status(self,id):
        service_question = ServiceQuestionModel.query.get(id)
        if not service_question.is_active:
            service_question.is_active = True
        else:
            service_question.is_active = False
        db.session.commit()
        return service_question.is_active