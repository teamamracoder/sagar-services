from db import db

class ProductQnAModel(db.Model):
    __tablename__ = "product_qnas"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_qnas_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    # updated_by is used as staff_id who wiil give answer
    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_qnas_updated_by"
        )
    )

    answered_at=db.Column(db.DateTime)

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
    answer = db.Column(db.Text)
   

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_questions_users"
        ),
        nullable=False
    )

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="product_qnas")
    products = db.relationship("ProductModel", back_populates="product_qnas")
    
