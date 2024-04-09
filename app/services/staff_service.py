from app.models import StaffModel
from .base_service import BaseService

class StaffService(BaseService):
    def __init__(self) -> None:
        super().__init__(StaffModel)

    def get_active(self):
        return StaffModel.query.filter_by(is_active=True).all()

    def get_by_user_id(self,user_id):
        return StaffModel.query.filter_by(user_id=user_id).first()