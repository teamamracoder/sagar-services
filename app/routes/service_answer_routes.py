from flask import Blueprint
from app.controllers import ServiceAnswerController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

service_answer_bp = Blueprint("service_answer", __name__)
service_answer_controller = ServiceAnswerController()


@service_answer_bp.route("/admin/service_answers/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return service_answer_controller.get()

@service_answer_bp.route("/admin/service_answers/data")
def get_service_answer_data():
    return service_answer_controller.get_service_answer_data()


@service_answer_bp.route("/admin/service_answers/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return service_answer_controller.create()

@service_answer_bp.route("/admin/service_answers/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return service_answer_controller.update(id)

@service_answer_bp.route("/admin/service_answers/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return service_answer_controller.status(id)
