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

@booking_bp.route("/admin/bookings/statuses/<string:status_type>/<string:status>/<string:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def statuses(status_type,status,id):
    return booking_controller.service_status(int(id),status_type,status)

@booking_bp.route("/admin/bookings/details/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return booking_controller.details(id)




## customer routes ##
@booking_bp.route("/my_bookings/")
@login_required
def bookings_page():
    return booking_controller.bookings_page()

@booking_bp.route("/my_bookings/data")
@login_required
def bookings_page_data():
    return booking_controller.bookings_page_data()

@booking_bp.route("/cancel/<int:booking_id>")
@login_required
def cancel(booking_id):
    return booking_controller.cancel(booking_id)

@booking_bp.route("/book_now/<int:service_id>")
@login_required
def booking_create_page(service_id):
    return booking_controller.booking_create(service_id)

@booking_bp.route("/book_now/confirm", methods=["GET","POST"])
@login_required
def confirm():
    return booking_controller.confirm()

@booking_bp.route("/booking_success")
@login_required
def booking_success():
    return booking_controller.booking_success()