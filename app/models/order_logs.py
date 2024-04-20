from db import db


class OrderLogModel(db.Model):
    __tablename__ = 'order_logs'

    id=db.Column(db.Integer, primary_key=True)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_order_logs_created_by"
        ),
        nullable=False
    )

    created_at = db.Column(db.DateTime)

    updated_by = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            name="fk_users_order_logs_updated_by"
        )
    )

    updated_at=db.Column(db.DateTime)

    is_active=db.Column(db.Boolean,default=True)

    order_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            "orders.id",
            name="fk_orders_order_logs"
        ),
        nullable=False,
    )
    order_status = db.Column(db.Integer(),nullable=False)

