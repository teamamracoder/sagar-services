from flask import Blueprint
from app.controllers import ProductQuestionController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

product_question_bp = Blueprint("product_question", __name__)
product_question_controller = ProductQuestionController()


@product_question_bp.route("/admin/product_questions/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return product_question_controller.get()

@product_question_bp.route("/admin/product_questions/data")
def get_product_question_data():
    return product_question_controller.get_product_question_data()


@product_question_bp.route("/admin/product_questions/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return product_question_controller.create()

@product_question_bp.route("/admin/product_questions/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return product_question_controller.update(id)

@product_question_bp.route("/admin/product_questions/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return product_question_controller.status(id)
