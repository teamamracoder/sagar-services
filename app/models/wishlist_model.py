from db import db
from datetime import datetime


class WishlistModel(db.Model):
    __tablename__ = 'wishlists'

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_wishlist_users_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_wishlist_users_updated_by"
        )
    )
    updated_at=db.Column(db.DateTime)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_wishlist_users"
        ),
        nullable=False
    )
    product_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            "products.id",
            name="fk_wishlist_product"
        ),
        nullable=False,
    )
    is_active = db.Column(db.Boolean, default=True)

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="wishlist")
    products = db.relationship("ProductModel")