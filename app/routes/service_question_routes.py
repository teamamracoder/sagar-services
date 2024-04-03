from flask import Blueprint
from flask_login import login_required
from app.controllers import ServiceQuestionController
service_question_controller = ServiceQuestionController()

service_question_bp = Blueprint("service_question_bp", __name__)


@service_question_bp.route("/admin/service_questions/")
@login_required
def index():
    return service_question_controller.get()

@service_question_bp.route("/admin/service_questions/data")
def get_service_question_data():
    return service_question_controller.get_service_question_data()

@service_question_bp.route("/admin/service_questions/add/", methods=["GET", "POST"])
@login_required
def add():
    return service_question_controller.create()


@service_question_bp.route("/admin/service_questions/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    return service_question_controller.update(id)


@service_question_bp.route("/admin/service_questions/status/<int:id>", methods=["GET", "POST"])
@login_required
def status(id):
    return service_question_controller.status(id)
