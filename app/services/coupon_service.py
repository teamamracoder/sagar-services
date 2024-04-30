from db import db
from app.models import CouponModel
from .base_service import BaseService
from app.constants import discount_types
from datetime import datetime

class CouponService(BaseService):
    def __init__(self) -> None:
        super().__init__(CouponModel)

    def add_discount_type_with_this(self, items):
        for item in items["data"]:
            item['discount_type_name']=discount_types.get_value(item["discount_type"])
        return items
    
    def get_by_code(self, coupon_code):
        today = datetime.now().date()

        # Query the Coupon model to find a coupon by its code, ensuring count > 0 and today < expiry_date
        coupon = self.model.query.filter(
            self.model.coupon_code == coupon_code,
            self.model.count > 0,
            self.model.expiry_date > today
        ).first()
        return coupon