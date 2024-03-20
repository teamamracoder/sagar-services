from db import db
from app.models import RoleModel


class RoleService:
    def create(self, user_id, role):
        role = RoleModel(user_id=user_id, role=role, created_by=1)
        db.session.add(role)
        db.session.commit()
        return role

    def get(self):
        return RoleModel.query.all()