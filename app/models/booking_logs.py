from db import db


class BookingLogModel(db.Model):
    __tablename__ = 'booking_logs'

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_booking_logs_created_by"
        ),
        nullable=False
    )

    created_at = db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_booking_logs_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    booking_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            "bookings.id",
            name="fk_bookings_booking_logs"
        ),
        nullable=False,
    )
    booking_status = db.Column(db.Integer(),nullable=False)