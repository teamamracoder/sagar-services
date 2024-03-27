from flask import Blueprint
from app.controllers import ServiceTypeController

service_type = Blueprint("service_type", __name__)
service_type_controller = ServiceTypeController()


@service_type.route("/admin/service_types/")
def index():
    return service_type_controller.get()


@service_type.route("/admin/service_types/add/", methods=["GET", "POST"])
def add():
    return service_type_controller.create()


@service_type.route("/admin/service_type/<int:id>/edit/", methods=["GET", "POST"])
def edit(id):
    return service_type_controller.update(id)


@service_type.route("/admin/service_types/<int:id>/status/", methods=["GET", "POST"])
def status(id):
    return service_type_controller.status(id)
