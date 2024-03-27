from flask import Blueprint
from flask_login import login_required

from app.controllers import HomeController

home_bp = Blueprint("home", __name__)
home_controller = HomeController()


@home_bp.route("/")
@login_required
def index():
    return home_controller.homepage()
