from app.models import RoleModel
from .base_service import BaseService
from app.constants import roles


class RoleService(BaseService):
    def __init__(self) -> None:
        super().__init__(RoleModel)

    def add_roles_with_users(self, users: list) -> list:
        for user in users["data"]:
            user["roles"] = self.get_roles_by_user_id(user["id"])
            user["not_in_roles"] = self.excluded_roles(user["roles"])
        return users

    def get_roles_by_user_id(self, user_id: int) -> dict:
        query = (
            RoleModel.query.filter_by(user_id=user_id,is_active=True)
            .with_entities(RoleModel.id, RoleModel.role)
            .all()
        )
        roles_dict = {key : roles.get_value(value) for key,value in query}
        return roles_dict
    
    def excluded_roles(self,user_has_roles):
        all_roles=roles.get_all_items_as_dict()
        excluded_roles = set(user_has_roles.values())
        result = {role: rolename for role, rolename in all_roles.items() if rolename not in excluded_roles}
        return result
    
    def get_role_by_user_id_and_role_key(self,role_key,user_id):
        return RoleModel.query.filter_by(role=role_key,user_id=user_id).first()
    

    def get_roles_by_user_id_list(self, user_id: int) -> list:
        if user_id:
            query = (
                RoleModel.query.filter_by(user_id=user_id, is_active=True)
                .with_entities(RoleModel.role)
                .all()
            )
            roles_list = [role[0] for role in query]
            return roles_list
        else:
            return []