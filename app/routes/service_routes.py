from flask import Blueprint, request, render_template
from app.controllers import ServiceController

service = Blueprint("service", __name__)
service_controller = ServiceController()


@service.route("/admin/services/")
def index():
    return service_controller.get()


@service.route("/admin/services/add/", methods=["GET", "POST"])
def add():
    return service_controller.create()

@service.route("/admin/services/<int:id>/edit/", methods=["GET", "POST"])
def edit(id):
    return service_controller.update(id)

@service.route("/admin/services/<int:id>/status/", methods=["GET", "POST"])
def status(id):
    return service_controller.status(id)


