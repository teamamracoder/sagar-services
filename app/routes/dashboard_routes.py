from flask import Blueprint
from flask_login import login_required
from app.auth import role_required
from app.controllers import DashboardController
from app.constants import roles

dashboard_bp = Blueprint("dashboard", __name__)
dashboard_controller = DashboardController()


@dashboard_bp.route("/admin/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return dashboard_controller.dashboard()
