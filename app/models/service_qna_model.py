from db import db
from datetime import datetime

class ServiceQnAModel(db.Model):
    __tablename__ = "service_qnas"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_qnas_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    # updated_by is used as staff_id who wiil give answer
    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_qnas_updated_by"
        )
    )

    answered_at=db.Column(db.DateTime)

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
    answer = db.Column(db.Text)
   

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_questions_users"
        ),
        nullable=False
    )

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="service_qnas")
    services = db.relationship("ServiceModel", back_populates="service_qnas")
    
