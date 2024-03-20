from db import db
from datetime import datetime


class ServiceTypeModel(db.Model):
    __tablename__ = "service_types"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_types_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime,default=datetime.now)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_types_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime,default=datetime.now)

    is_active=db.Column(db.Boolean,default=True)

    type_name = db.Column(db.String(200),nullable=False)

    service_img_url = db.Column(db.Text)

    services = db.relationship("ServiceModel", back_populates="service_types")
    created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="service_type_created")
    updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="service_type_updated")