from flask import Blueprint
from app.controllers import ServiceQuestionController

service_question = Blueprint("service_question", __name__)
service_question_controller = ServiceQuestionController()


@service_question.route("/admin/service_questions/")
def index():
    return service_question_controller.get()


@service_question.route("/admin/service_questions/add/", methods=["GET", "POST"])
def add():
    return service_question_controller.create()

@service_question.route("/admin/service_questions/<int:id>/edit/", methods=["GET", "POST"])
def edit(id):
    return service_question_controller.update(id)


@service_question.route("/admin/service_question/<int:id>/status/", methods=["GET", "POST"])
def status(id):
    return service_question_controller.status(id)

