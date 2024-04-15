from flask import Blueprint
from app.controllers import ServiceReviewController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
service_review_bp = Blueprint("service_review", __name__)
service_review_controller = ServiceReviewController()

    
@service_review_bp.route("/admin/service_reviews/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return service_review_controller.get()

@service_review_bp.route("/admin/service_reviews/data")
def get_service_review_data():
    return service_review_controller.get_service_review_data()


@service_review_bp.route("/admin/service_reviews/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return service_review_controller.create()
    

@service_review_bp.route("/admin/service_reviews/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return service_review_controller.status(id)
