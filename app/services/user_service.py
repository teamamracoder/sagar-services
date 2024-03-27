from db import db
from app.models import UserModel


class UserService:
    def create(self, **kwargs):
        user = UserModel(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    def get(self):
        return UserModel.query.all()

    def get_by_id(self, id):
        return UserModel.query.get(id)

    def get_user_by_email_and_password(self, email, password):
        return UserModel.query.filter_by(email=email, password=password).first()
