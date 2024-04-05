from db import db
from datetime import datetime

class ServiceQuestionModel(db.Model):
    __tablename__ = "service_questions"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_questions_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_questions_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    service_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "services.id",
            name="fk_questions_services"
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

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="service_questions")
    services = db.relationship("ServiceModel", back_populates="service_questions")
    service_answers = db.relationship("ServiceAnswerModel", back_populates="service_questions", uselist=False)

