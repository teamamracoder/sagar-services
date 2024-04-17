from flask import Blueprint
from app.controllers import AboutUsController

about_us_bp = Blueprint("about_us", __name__)
about_us_controller = AboutUsController()


@about_us_bp.route("/about_us/")
def about_us_page():
    return about_us_controller.about_us_page()