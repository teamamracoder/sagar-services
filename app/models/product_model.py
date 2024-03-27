from db import db
from datetime import datetime

class ProductModel(db.Model):
    __tablename__="products"

    id=db.Column(db.Integer, primary_key=True)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "categories.id",
            name="fk_product_categories"
        ),
        nullable=False
    )

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_products_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime,default=datetime.now)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_products_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime,default=datetime.now)

    is_active=db.Column(db.Boolean,default=True)

    product_name=db.Column(db.String(100),nullable=False)

    brand=db.Column(db.String(100),nullable=False)

    model=db.Column(db.String(100),nullable=False)

    price=db.Column(db.Double,nullable=False)

    discount=db.Column(db.Double)

    stock=db.Column(db.Integer,nullable=False)



    product_img_urls=db.Column(db.ARRAY(db.Text),default=[])

    specifications=db.Column(db.String(2000),nullable=False)

    payment_methods=db.Column(db.ARRAY(db.Integer),nullable=False)

    available_area_pincodes=db.Column(db.ARRAY(db.String(6)),nullable=False)

    return_policy=db.Column(db.String())

    # user = db.relationship("UserModel", back_populates="products")

    categories = db.relationship("CategoryModel",uselist=False,back_populates="products")
    # created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="product_created")
    # updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="product_updated")
    orders = db.relationship("OrderModel",back_populates="products")
    product_reviews = db.relationship("ProductReviewModel",back_populates="products")
    product_questions = db.relationship("ProductQuestionModel", back_populates="products")
    # product_reviews = db.relationship("ProductReviewModel", back_populates="products")
    # orders = db.relationship("OrderModel", back_populates="products")
    # carts = db.relationship("CartModel", back_populates="products")
    # wishlists = db.relationship("WishlistModel", back_populates="products")
    # product_questions = db.relationship("ProductQuestionModel", back_populates="products")
