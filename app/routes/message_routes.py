from flask import Blueprint
from flask_login import login_required

from app.auth import role_required
from app.controllers import MessageController

message_bp = Blueprint("message", __name__)
message_controller = MessageController()


@message_bp.route("/admin/messages/")
def index():
    return message_controller.get()

@message_bp.route("/admin/messages/data")
def get_message_data():
    return message_controller.get_message_data()

@message_bp.route("/admin/messages/add/", methods=["GET", "POST"])
@login_required
@role_required([1, 2])
def add():
    return message_controller.create()

@message_bp.route("/admin/messages/update/<int:id>", methods=["GET", "POST"])
def update(id):
    return message_controller.update(id)


@message_bp.route("/admin/messages/status/<int:id>", methods=["GET", "PATCH"])
def status(id):
    return message_controller.status(id)
