from db import db
from datetime import datetime


class ConversationModel(db.Model):
    __tablename__="conversations"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_converations_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_converations_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_converations_user"
        ),
        nullable=False
    )

    staff_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_converations_staff"
        ),
        nullable=False
    )
    users = db.relationship('UserModel', foreign_keys=[user_id], backref="conversation_users")
    staffs = db.relationship('UserModel', foreign_keys=[staff_id], backref="conversation_staffs")
    messages = db.relationship("MessageModel", back_populates="conversations")
    created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="conversation_created")
    updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="conversation_updated")