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


@user_bp.route("/admin/users/details/<int:id>", methods=["GET"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return user_controller.details(id)

@user_bp.route("/admin/users/my_profile/", methods=["GET"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def admin_my_profile():
    return user_controller.admin_my_profile()

@user_bp.route("/admin/users/my_profile/",  methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def admin_my_profile_update():
    return user_controller.admin_my_profile_update()




## customer routes ##

@user_bp.route("/my_profile/", methods=["GET", "POST"])
@login_required
def my_profile_page():
    return user_controller.my_profile_page()

@user_bp.route("/my_profile/update", methods=["GET", "POST"])
@login_required
def my_profile_update():
    return user_controller.my_profile_update()