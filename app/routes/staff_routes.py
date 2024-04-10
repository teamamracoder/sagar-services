from flask import Blueprint
from app.controllers import StaffController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
staff_bp = Blueprint("staff", __name__)
staff_controller = StaffController()

    
@staff_bp.route("/admin/staffs/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return staff_controller.get()

@staff_bp.route("/admin/staffs/data")
def get_staff_data():
    return staff_controller.get_staff_data()


@staff_bp.route("/admin/staffs/add/<int:user_id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def add(user_id):
    return staff_controller.create(user_id)


@staff_bp.route("/admin/staffs/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def update(id):
    return staff_controller.update(id)


@staff_bp.route("/admin/staffs/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN")])
def status(id):
    return staff_controller.status(id)

@staff_bp.route("/admin/staffs/details/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return staff_controller.details(id)
