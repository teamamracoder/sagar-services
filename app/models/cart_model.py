from db import db
from datetime import datetime


class CartModel(db.Model):
    __tablename__ = "carts"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_carts_created_by"
        ),
        nullable=False
    )

    created_at = db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_carts_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_user_id_users"
        ),
        nullable=False
    )

    status = db.Column(db.Integer)

    product_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            "products.id",
            name="fk_cart_product"
        ),
        nullable=False,
    )

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="cart")
    products = db.relationship("ProductModel")