from flask import Blueprint
from flask_login import login_required

from app.auth import role_required
from app.controllers import UserController

user_bp = Blueprint("user_bp", __name__)
user_controller = UserController()


@user_bp.route("/admin/users/")
def index():
    return user_controller.get()


@user_bp.route("/admin/users/add/", methods=["GET", "POST"])
@login_required
@role_required([1, 2])
def add():
    return user_controller.create()
