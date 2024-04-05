from flask import Blueprint
from flask_login import login_required

from app.auth import role_required
from app.controllers import ConversationController

conversation_bp = Blueprint("conversation", __name__)
conversation_controller = ConversationController()


@conversation_bp.route("/admin/conversations/")
@login_required
@role_required([1, 2])
def index():
    return conversation_controller.get()

@conversation_bp.route("/admin/conversations/data")
def get_conversation_data():
    return conversation_controller.get_conversation_data()

@conversation_bp.route("/admin/conversations/add/", methods=["GET", "POST"])
@login_required
@role_required([1, 2])
def add():
    return conversation_controller.create()

@conversation_bp.route("/admin/conversations/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([1, 2])
def update(id):
    return conversation_controller.update(id)


@conversation_bp.route("/admin/conversations/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([1, 2])
def status(id):
    return conversation_controller.status(id)
