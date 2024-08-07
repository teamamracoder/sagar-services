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


@cart_bp.route("/admin/carts/update/<int:id>/<string:status>", methods=["GET", "POST"])
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

@cart_bp.route("/cart/data/")
@login_required
def cart_page_data():
    return cart_controller.cart_page_data()

@cart_bp.route("/cart/add/<int:product_id>")
def add(product_id):
    return cart_controller.create(product_id)

@cart_bp.route("/cart/status/<int:id>", methods=["GET", "PATCH"])
def add_or_remove(id):
    return cart_controller.status(id)