from flask import Blueprint
from flask_login import login_required
from app.controllers import ServiceTypeController
from app.constants import roles
from app.auth import role_required

service_type_controller = ServiceTypeController()

service_type_bp = Blueprint("service_type", __name__)


@service_type_bp.route("/admin/service_types/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return service_type_controller.get()

@service_type_bp.route("/admin/service_types/data")
def get_service_type_data():
    return service_type_controller.get_service_type_data()

@service_type_bp.route("/admin/service_types/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return service_type_controller.create()


@service_type_bp.route("/admin/service_types/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return service_type_controller.update(id)


@service_type_bp.route("/admin/service_types/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return service_type_controller.status(id)
