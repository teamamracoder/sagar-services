from flask import Blueprint
from flask_login import login_required

from app.auth import role_required
from app.controllers import MessageController

message_bp = Blueprint("message", __name__)
message_controller = MessageController()


@message_bp.route("/admin/messages/<int:conversation_id>")
@login_required
@role_required([1, 2])
def index(conversation_id):
    return message_controller.get(conversation_id)

# @message_bp.route("/admin/messages/data")
# def get_message_data():
#     return message_controller.get_message_data()

@message_bp.route("/admin/messages/add/<int:conversation_id>", methods=["GET", "POST"])
@login_required
@role_required([1, 2])
def add(conversation_id):
    return message_controller.create(conversation_id)

# @message_bp.route("/admin/messages/update/<int:id>", methods=["GET", "POST"])
# @login_required
# @role_required([1, 2])
# def update(id):
#     return message_controller.update(id)


@message_bp.route("/admin/messages/status/<int:id>/<int:conversation_id>", methods=["GET", "PATCH"])
@login_required
@role_required([1, 2])
def status(id,conversation_id):
    return message_controller.status(id,conversation_id)
