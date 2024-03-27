from db import db
from app.models import CouponModel


class CouponService:
    def create(self, **kwargs):
        coupon = CouponModel(**kwargs)
        db.session.add(coupon)
        db.session.commit()
        return coupon

    def get(self):
        return CouponModel.query.all()
