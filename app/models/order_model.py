from db import db
from datetime import datetime


class OrderModel(db.Model):
    __tablename__="orders"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_order_created_by"
        ),
        nullable=False
    )

    created_at = db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_order_updated_by"
        )
    )

    updated_at = db.Column(db.DateTime)

    is_active = db.Column(db.Boolean,default=True)

    product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "products.id",
            name="fk_orders_products"
        ),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_bookings"
        ),
        nullable=False
    )

    quantity=db.Column(db.Integer,nullable=False)

    price=db.Column(db.Double,nullable=False)

    payment_method=db.Column(db.Integer,nullable=False)

    order_status=db.Column(db.Integer)

    shipping_address=db.Column(db.String(200),nullable=False)

    payment_status=db.Column(db.Integer)

    area_pincode=db.Column(db.Integer,nullable=False)

    expected_delivery = db.Column(db.Date)

    mobile = db.Column(db.String(15))

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="orders")
    products = db.relationship("ProductModel",back_populates="orders")
    # created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="orders_created")
    # updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="orders_updated")