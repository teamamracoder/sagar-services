from flask import Blueprint
from app.controllers import AboutUsController

about_us_bp = Blueprint("about_us", __name__)
about_us_controller = AboutUsController()


@about_us_bp.route("/about_us/")
def index():
    return about_us_controller.customer_get()