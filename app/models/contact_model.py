from db import db
from datetime import datetime


class ContactModel(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_coupons_created_by"
        )
    )

    created_at = db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_coupons_updated_by"
        )
    )

    updated_at = db.Column(db.DateTime)

    is_active = db.Column(db.Boolean, default=True)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    query_message = db.Column(db.Text, nullable=False)
    query_img_urls=db.Column(db.ARRAY(db.Text),default=[])
