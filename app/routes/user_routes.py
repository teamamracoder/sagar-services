from flask import Blueprint
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
from app.controllers import UserController

user_bp = Blueprint("user", __name__)
user_controller = UserController()


@user_bp.route("/admin/users/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return user_controller.get()


@user_bp.route("/admin/users/data")
def get_user_data():
    return user_controller.get_user_data()


@user_bp.route("/admin/users/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def add():
    return user_controller.create()


@user_bp.route("/admin/users/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def update(id):
    return user_controller.update(id)


@user_bp.route("/admin/users/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def status(id):
    return user_controller.status(id)


@user_bp.route("/admin/users/details/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return user_controller.details(id)
