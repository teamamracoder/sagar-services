from flask import Blueprint
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
from app.controllers import ContactController

contact_bp = Blueprint("contact_bp", __name__)
contact_controller = ContactController()


@contact_bp.route("/admin/contacts/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return contact_controller.get()


@contact_bp.route("/admin/contacts/data")
def get_contact_data():
    return contact_controller.get_contact_data()


@contact_bp.route("/admin/contacts/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def add():
    return contact_controller.create()


@contact_bp.route("/admin/contacts/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def update(id):
    return contact_controller.update(id)


@contact_bp.route("/admin/contacts/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def status(id):
    return contact_controller.status(id)
