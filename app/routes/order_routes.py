from flask import Blueprint
from app.controllers import OrderController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
order_bp = Blueprint("order", __name__)
order_controller = OrderController()


@order_bp.route("/admin/orders/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return order_controller.get()

@order_bp.route("/admin/orders/data")
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def get_order_data():
    return order_controller.get_order_data()


@order_bp.route("/admin/orders/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF"),roles.get_key("CUSTOMER")])
def add():
    return order_controller.create()


@order_bp.route("/admin/orders/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return order_controller.update(id)


@order_bp.route("/admin/orders/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return order_controller.status(id)

@order_bp.route("/admin/orders/statuses/<string:status_type>/<string:status>/<string:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def statuses(id,status_type,status):
    return order_controller.order_status(int(id),status_type,status)

@order_bp.route("/admin/orders/details/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return order_controller.details(id)



## customer routes ##

@order_bp.route("/my_orders/")
@login_required
def orders_page():
    return order_controller.orders_page()

@order_bp.route("/my_orders/data")
@login_required
def orders_page_data():
    return order_controller.orders_page_data()

@order_bp.route("/cancel/<int:order_id>")
@login_required
def cancel(order_id):
    return order_controller.cancel(order_id)


@order_bp.route("/order_details/<int:order_id>")
@login_required
def order_details_page(order_id):
    return order_controller.order_details_page(order_id)


