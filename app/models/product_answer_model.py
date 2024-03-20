from db import db
from datetime import datetime


class ProductAnswerModel(db.Model):

    __tablename__ = "product_answers"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_answer_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.Date,default=datetime.now)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_product_answer_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime,default=datetime.now)

    is_active=db.Column(db.Boolean,default=True)

    question_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "product_questions.id",
            name="fk_product_answers_product_questions"
        ),
        nullable=False
    )
    staff_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_answers_staffs"
        ),
        nullable=False
    )
    answer = db.Column(db.Text, nullable=False)

    users = db.relationship('UserModel', foreign_keys=[staff_id], backref="product_answers")
    product_questions=db.relationship("ProductQuestionModel", back_populates="product_answers",uselist=False)