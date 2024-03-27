from db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id=db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(100),nullable=False)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_categories_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_categories_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)


    category_img_url=db.Column(db.Text)


    products = db.relationship("ProductModel", back_populates="categories")
    created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="category_created")
    updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="category_updated")
    # users = db.relationship("UserModel", back_populates="categories")
