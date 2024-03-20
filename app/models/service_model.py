from db import db
from datetime import datetime

class ServiceModel(db.Model):
    __tablename__="services"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_services_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime,default=datetime.now)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_services_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime,default=datetime.now)

    is_active=db.Column(db.Boolean,default=True)

    service_name = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    service_charge = db.Column(db.Double, nullable=False)

    available_area_pincode = db.Column(db.ARRAY(db.Integer),default=[])

    payment_methods = db.Column(db.ARRAY(db.Integer),default=[])

    discount = db.Column(db.Double)

    service_img_urls = db.Column(db.ARRAY(db.Text),default=[])

    service_type_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'service_types.id'
        ),
        nullable=False
    )

    service_types = db.relationship("ServiceTypeModel", uselist=False, back_populates="services")
    # created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="service_created")
    # updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="service_updated")
    bookings = db.relationship("BookingModel", back_populates="services")
    service_reviews = db.relationship("ServiceReviewModel", back_populates="services")
    service_questions = db.relationship("ServiceQuestionModel", back_populates="services")

