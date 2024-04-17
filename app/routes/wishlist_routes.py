from flask import Blueprint
from app.controllers import WishlistController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

wishlist_bp = Blueprint("wishlist", __name__)
wishlist_controller = WishlistController()


@wishlist_bp.route("/admin/wishlists/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return wishlist_controller.get()


@wishlist_bp.route("/admin/wishlists/data")
def get_wishlist_data():
    return wishlist_controller.get_wishlist_data()


@wishlist_bp.route("/admin/wishlists/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return wishlist_controller.create()


@wishlist_bp.route("/admin/wishlists/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return wishlist_controller.status(id)



## customer routes ##

@wishlist_bp.route("/wishlist/")
@login_required
def wishlist_page():
    return wishlist_controller.wishlist_page()