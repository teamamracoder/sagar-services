from flask import Blueprint
from app.controllers import CartController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

cart_bp = Blueprint("cart", __name__)
cart_controller = CartController()


@cart_bp.route("/admin/carts/")
def index():
    return cart_controller.get()


@cart_bp.route("/admin/carts/data")
def get_cart_data():
    return cart_controller.get_cart_data()


#add by admin
@cart_bp.route("/admin/carts/add/", methods=["GET", "POST"])
@login_required
def add():
    return cart_controller.create()

#add by customer
@cart_bp.route("/admin/carts/add_to_cart/", methods=["GET", "POST"])
@login_required
def add_to_cart(product_id):
    return cart_controller.add_to_cart(product_id)


@cart_bp.route("/admin/carts/update/<int:cart_id>/<string:status>", methods=["GET", "POST"])
@login_required
def update(cart_id, status):
    return cart_controller.cart_status(cart_id, status)


@cart_bp.route("/admin/carts/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return cart_controller.status(id)
