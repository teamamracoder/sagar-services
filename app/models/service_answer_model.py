from db import db
from datetime import datetime

class ServiceAnswerModel(db.Model):
    __tablename__ = "service_answers"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_answers_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.Date,default=datetime.now)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_answers_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime,default=datetime.now)

    is_active=db.Column(db.Boolean,default=True)

    question_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "service_questions.id",
            name="fk_service_answers_service_questions"
        ),
        nullable=False
    )

    answer = db.Column(db.Text, nullable=False)

    staff_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_answers_staffs"
        ),
        nullable=False
    )
    service_questions = db.relationship("ServiceQuestionModel", back_populates="service_answers", uselist=False)
    users = db.relationship('UserModel', foreign_keys=[staff_id], backref="service_answers")
