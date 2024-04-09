from flask import Blueprint
from app.controllers import BookingController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

booking_bp = Blueprint("booking", __name__)
booking_controller = BookingController()

    
@booking_bp.route("/admin/bookings/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return booking_controller.get()

@booking_bp.route("/admin/bookings/data")
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def get_booking_data():
    return booking_controller.get_booking_data()


@booking_bp.route("/admin/bookings/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF"),roles.get_key("CUSTOMER")])
def add():
    return booking_controller.create()


@booking_bp.route("/admin/bookings/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return booking_controller.update(id)


@booking_bp.route("/admin/bookings/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return booking_controller.status(id)

@booking_bp.route("/admin/bookings/statuses/<int:id>/<string:status_type>/<string:status>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def statuses(id,status_type,status):
    return booking_controller.service_status(id,status_type,status)