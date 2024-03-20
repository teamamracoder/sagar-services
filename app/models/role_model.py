from db import db
from datetime import datetime


class RoleModel(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_role"
        ),
        nullable=False
    )
    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_role_created_by"
        ),
        nullable=False
    )
    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_role_updated_by"
        )
    )
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    is_active = db.Column(db.Boolean, default=True)

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="roles")


    # created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="roles_created")
    # updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="roles_updated")
