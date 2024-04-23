from flask import Blueprint
from app.controllers import ServiceQnAController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
service_qna_bp = Blueprint("service_qna", __name__)
service_qna_controller = ServiceQnAController()

    
@service_qna_bp.route("/admin/service_qnas/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return service_qna_controller.get()

@service_qna_bp.route("/admin/service_qnas/data")
def get_service_qna_data():
    return service_qna_controller.get_service_qna_data()


@service_qna_bp.route("/admin/service_qnas/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return service_qna_controller.create()


@service_qna_bp.route("/admin/service_qnas/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return service_qna_controller.update(id)


@service_qna_bp.route("/admin/service_qnas/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return service_qna_controller.status(id)



# customer
@service_qna_bp.route("/service_qnas/<int:service_id>", methods=["GET","POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF"), roles.get_key("CUSTOMER")])
def service_qna_create(service_id):
    return service_qna_controller.service_qna_create(service_id)
