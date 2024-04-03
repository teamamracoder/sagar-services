from flask import Blueprint, request, render_template
from app.controllers import ServiceController
from flask_login import login_required

service_controller = ServiceController()

service_bp = Blueprint("service_bp", __name__)


@service_bp.route("/admin/services/")
@login_required
def index():
    return service_controller.get()

@service_bp.route("/admin/services/data")
def get_service_data():
    return service_controller.get_service_data()



@service_bp.route("/admin/services/add/", methods=["GET", "POST"])
@login_required
def add():
    return service_controller.create()

@service_bp.route("/admin/services/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    return service_controller.update(id)

@service_bp.route("/admin/services/status/<int:id>", methods=["GET", "POST"])
@login_required
def status(id):
    return service_controller.status(id)


