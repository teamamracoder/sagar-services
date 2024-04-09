from app.models import StaffModel
from .base_service import BaseService
from app.constants import departments

class StaffService(BaseService):
    def __init__(self) -> None:
        super().__init__(StaffModel)

    def get_active(self):
        return StaffModel.query.filter_by(is_active=True).all()

    def get_by_user_id(self,user_id):
        return StaffModel.query.filter_by(user_id=user_id).first()
    
    def add_departments_with_this(self, items):
        for item in items["data"]:
            item['department_name']=departments.get_value(item["department"])
        return items