from flask import Blueprint, request, render_template
from app.controllers import ServiceController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
from urllib.parse import unquote


service_bp = Blueprint("service", __name__)

service_controller = ServiceController()

@service_bp.route("/admin/services/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return service_controller.get()

@service_bp.route("/admin/services/data")
def get_service_data():
    return service_controller.get_service_data()

@service_bp.route("/admin/services/total_price")
def get_total_price():
    return service_controller.get_total_price()

@service_bp.route("/admin/services/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return service_controller.create()

@service_bp.route("/admin/services/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return service_controller.update(id)

@service_bp.route("/admin/services/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return service_controller.status(id)

@service_bp.route("/admin/services/details/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return service_controller.details(id)

@service_bp.route("/admin/services/addimage/<int:service_id>", methods=["GET","POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def addImage(service_id):
    return service_controller.addImage(service_id)

@service_bp.route("/admin/services/deleteImage/<int:service_id>/<path:filename>")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def deleteImage(service_id,filename):
    filename = unquote(filename)
    return service_controller.deleteImage(service_id,filename)



# customer routes

# @service_bp.route("/service_page/", methods=["GET", "POST"])
# def service_page():
#     return service_controller.service_page()


@service_bp.route("/service_details/<int:service_id>", methods=["GET", "PATCH"])
def service_details_page(service_id):
    return service_controller.service_details_page(service_id)

@service_bp.route("/check_area_availability/", methods=[ "POST"])
def check_area_availability():
    return service_controller.check_area_availability()

