from flask import Blueprint
from app.controllers import ProductAnswerController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required

product_answer_bp = Blueprint("product_answer", __name__)
product_answer_controller = ProductAnswerController()


@product_answer_bp.route("/admin/product_answers/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return product_answer_controller.get()

@product_answer_bp.route("/admin/product_answers/data")
def get_product_answer_data():
    return product_answer_controller.get_product_answer_data()


@product_answer_bp.route("/admin/product_answers/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return product_answer_controller.create()

@product_answer_bp.route("/admin/product_answers/add/<int:question_id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add_for_question(question_id):
    return product_answer_controller.create_for_question(question_id)

@product_answer_bp.route("/admin/product_answers/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return product_answer_controller.update(id)

@product_answer_bp.route("/admin/product_answers/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return product_answer_controller.status(id)
