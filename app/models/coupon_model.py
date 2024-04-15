from db import db
from datetime import datetime


class CouponModel(db.Model):

    __tablename__ = "coupons"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_coupons_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_coupons_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    coupon_code = db.Column(db.String(50),unique=True, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    discount_type = db.Column(db.Integer)
    discount = db.Column(db.Float, nullable=False)
    coupon_img_url = db.Column(db.Text)
    count = db.Column(db.Integer, nullable=False)