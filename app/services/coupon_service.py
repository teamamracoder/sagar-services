from db import db
from app.models import CouponModel
from .base_service import BaseService
from app.constants import discount_types

class CouponService(BaseService):
    def __init__(self) -> None:
        super().__init__(CouponModel)

    def add_discount_type_with_this(self, items):
        for item in items["data"]:
            item['discount_type_name']=discount_types.get_value(item["discount_type"])
        return items