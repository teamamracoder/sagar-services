from db import db
from datetime import datetime


class ServiceReviewModel(db.Model):
    __tablename__="service_reviews"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_reviews_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_reviews_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_service_reviews"
        ),
        nullable=False
    )

    review_title=db.Column(db.String(400))

    description=db.Column(db.String(400),nullable=False)

    img_urls=db.Column(db.ARRAY(db.String(200)))

    rating=db.Column(db.Double,nullable=False)

    service_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "services.id",
            name="fk_service_reviews_services"
        ),
        nullable=False
    )

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="service_reviews")
    services = db.relationship("ServiceModel", back_populates="service_reviews")
    created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="service_reviews_created")
    updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="service_reviews_updated")