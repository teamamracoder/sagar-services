from flask import Blueprint
from flask_login import login_required
from app.controllers import ServiceQuestionController
from app.constants import roles
from app.auth import role_required

service_question_controller = ServiceQuestionController()

service_question_bp = Blueprint("service_question", __name__)


@service_question_bp.route("/admin/service_questions/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return service_question_controller.get()

@service_question_bp.route("/admin/service_questions/data")
def get_service_question_data():
    return service_question_controller.get_service_question_data()

@service_question_bp.route("/admin/service_questions/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return service_question_controller.create()


@service_question_bp.route("/admin/service_questions/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return service_question_controller.update(id)


@service_question_bp.route("/admin/service_questions/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return service_question_controller.status(id)
