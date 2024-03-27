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
