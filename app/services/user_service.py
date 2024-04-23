from app.models import UserModel
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self) -> None:
        super().__init__(UserModel)

    def get_user_by_email_and_password(self, email, password):
        return UserModel.query.filter_by(email=email, password=password).first()

    def add_user_with_this(self, items: dict) -> dict:
        for item in items["data"]:
            user = self.get_by_id(item["user_id"])
            item["fullname"] = user.first_name + " " + user.last_name
            item["email"] = user.email
        return items

    def add_message_with_this(self, messages: dict) -> dict:
        for message in messages:
            message.sent_by = self.get_by_id(message.created_by).first_name
        return messages

    def get_user_by_id(self,id):
        return UserModel.query.filter_by(id=id).all()


    def get_user_by_reviews_for_home(self, datas) -> dict:
        for data in datas:
            reviews = data["service_review"]
            serialized_users = []
            for review in reviews:
                users = self.get_user_by_id(review["user_id"])
                serialized_user = [self.serialize_users(user) for user in users]
                serialized_users.extend(serialized_user)
            data["serialized_users"] = serialized_users
        return datas


    def serialize_users(self, user):
        return {key: getattr(user, key) for key in user.__dict__ if not key.startswith("_")}

    def get_user_by_email(self, email):
        return UserModel.query.filter_by(email=email).first()

    def get_user_by_mobile(self, mobile):
        return UserModel.query.filter_by(mobile=mobile).first()
