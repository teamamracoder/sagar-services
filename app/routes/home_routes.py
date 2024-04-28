from flask import Blueprint
from app.controllers import HomeController

home_bp = Blueprint("home", __name__)
home_controller = HomeController()


@home_bp.route("/")
def index():
    return home_controller.homepage()

@home_bp.route("/", methods=["GET", "POST"])
def get_total_cart_and_wish():
    return home_controller.get_total_cart_and_wish()
