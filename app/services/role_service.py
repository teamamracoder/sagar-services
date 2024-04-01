from db import db
from app.models import RoleModel
from .base_service import BaseService
from app.constants import roles


class RoleService(BaseService):
    def __init__(self) -> None:
        super().__init__(RoleModel)

    def add_roles_with_users(self, users: list) -> list:
        for user in users["data"]:
            user["roles"] = self.get_roles_by_user_id(user["id"])
        return users

    def get_roles_by_user_id(self, user_id: int) -> list:
        query = (
            RoleModel.query.filter_by(user_id=user_id,is_active=True)
            .with_entities(RoleModel.role)
            .all()
        )
        role_list = [roles.get_value(row[0]) for row in query]
        return role_list
