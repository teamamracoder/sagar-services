from db import db
from datetime import datetime


class ProductReviewModel(db.Model):
    __tablename__="product_reviews"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_reviews_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_reviews_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_reviews"
        ),
        nullable=False
    )

    review_title=db.Column(db.String(100))

    description=db.Column(db.String(200),nullable=False)

    product_review_img_urls=db.Column(db.ARRAY(db.Text))

    rating=db.Column(db.Double,nullable=False)

    product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "products.id",
            name="fk_product_reviews_products"
        ),
        nullable=False
    )

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="product_reviews")
    products = db.relationship("ProductModel")
    # created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="product_reviews_created")
    # updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="product_reviews_updated")
