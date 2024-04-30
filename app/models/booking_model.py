from db import db
from datetime import datetime

class BookingModel(db.Model):
    __tablename__="bookings"

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_bookings_created_by"
        ),
        nullable=False
    )

    created_at=db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_bookings_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    service_id=db.Column(
        db.Integer,
        db.ForeignKey(
            "services.id",
            name="fk_booking_service"
        ),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_bookings_user"
        ),
        nullable=False
    )

    staff_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "staffs.id",
            name="fk_bookings_staff"
        )
    )

    total_charges=db.Column(db.Double,nullable=False)

    service_location=db.Column(db.Text,nullable=False)

    service_status=db.Column(db.Integer)

    payment_status=db.Column(db.Integer)

    payment_method=db.Column(db.Integer,nullable=False)

    area_pincode=db.Column(db.Integer,nullable=False)

    booking_details=db.Column(db.Text)

    mobile = db.Column(db.String(15))

    users = db.relationship('UserModel', foreign_keys=[user_id], backref="bookings_users")
    staffs = db.relationship('StaffModel', foreign_keys=[staff_id], backref="bookings_staffs")
    services = db.relationship("ServiceModel", back_populates="bookings")
    created_by_id = db.relationship("UserModel", foreign_keys=[created_by], backref="booking_created")
    updated_by_id = db.relationship("UserModel", foreign_keys=[updated_by], backref="booking_updated")

