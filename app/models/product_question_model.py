from db import db
from datetime import datetime

class ProductQuestionModel(db.Model):
    __tablename__ = "product_questions"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_questions_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.Date,default=datetime.now)
    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_questions_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime,default=datetime.now)

    is_active=db.Column(db.Boolean,default=True)

    product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "products.id",
            name="fk_questions_products"
        ),
        nullable=False
    )
    question = db.Column(db.Text, nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_questions_users"
        ),
        nullable=False
    )

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="product_questions")
    products = db.relationship("ProductModel",back_populates="product_questions")
    product_answers = db.relationship("ProductAnswerModel", back_populates="product_questions",uselist=False)