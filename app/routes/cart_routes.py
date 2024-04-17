from flask import Blueprint
from app.controllers import CartController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

cart_bp = Blueprint("cart", __name__)
cart_controller = CartController()


@cart_bp.route("/admin/carts/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return cart_controller.get()


@cart_bp.route("/admin/carts/data")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def get_cart_data():
    return cart_controller.get_cart_data()


@cart_bp.route("/admin/carts/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
@login_required
def add():
    return cart_controller.create()


# update will be used to update the cart statue as added/ordered/removed
@cart_bp.route("/admin/carts/update/<int:id>/<string:status>", methods=["GET", "POST"])
@login_required
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id, status):
    return cart_controller.cart_status(id, status)


@cart_bp.route("/admin/carts/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return cart_controller.status(id)




## customer routes ##

@cart_bp.route("/cart/")
@login_required
def cart_page():
    return cart_controller.cart_page()