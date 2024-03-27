from flask import Blueprint

from app.controllers import HomeController

home_bp = Blueprint("home_bp", __name__)
home_controller = HomeController()


@home_bp.route("/")
def index():
    return home_controller.homepage()
