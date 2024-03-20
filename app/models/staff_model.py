from db import db
from datetime import datetime


class StaffModel(db.Model):
    __tablename__ = 'staffs'

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_staffs_users_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.Date,default=datetime.now)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_staffs_users_updated_by"
        )
    )
    updated_at=db.Column(db.DateTime,default=datetime.now)
    is_active=db.Column(db.Boolean,default=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_staffs_users"
        ),
        nullable=False,
        unique=True
    )

    salary = db.Column(db.Double, nullable=False)
    qualification = db.Column(db.String(80), nullable=False)
    join_date = db.Column(db.DateTime, nullable=False)
    leave_date = db.Column(db.DateTime)
    department = db.Column(db.Integer, nullable=False)

    users=db.relationship("UserModel", foreign_keys=[user_id],backref="staff",uselist=False)