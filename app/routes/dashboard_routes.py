from flask import Blueprint
from flask_login import login_required

from app.controllers import DashboardController

dashboard_bp = Blueprint("dashboard", __name__)
dashboard_controller = DashboardController()


@dashboard_bp.route("/admin/")
# @login_required
def index():
    return dashboard_controller.dashboard()
