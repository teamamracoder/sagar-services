from db import db
from datetime import datetime

class MessageModel(db.Model):
    __tablename__="messages"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_messages_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_messages_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    conversation_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "conversations.id",
            name="fk_conversations_messages"
        ),
        nullable=False
    )

    message_text=db.Column(db.String(400),nullable=False)
    attachament_url=db.Column(db.String(200))
    read_status=db.Column(db.Boolean,default=False)

    conversations = db.relationship("ConversationModel", back_populates="messages")
    created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="message_created")
    updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="message_updated")