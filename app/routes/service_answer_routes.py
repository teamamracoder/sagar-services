from flask import Blueprint
from app.controllers import ServiceAnswerController

service_answer = Blueprint("service_answer", __name__)
service_answer_controller = ServiceAnswerController()


@service_answer.route("/admin/service_answers/")
def index():
    return service_answer_controller.get()


@service_answer.route("/admin/service_answers/add/", methods=["GET", "POST"])
def add():
    return service_answer_controller.create()

@service_answer.route("/admin/service_answers/<int:id>/edit/", methods=["GET", "POST"])
def edit(id):
    return service_answer_controller.update(id)

@service_answer.route("/admin/service_answers/<int:id>/status/", methods=["GET", "POST"])
def status(id):
    return service_answer_controller.status(id)
