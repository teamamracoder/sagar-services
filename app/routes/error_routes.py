from flask import Blueprint

from app.controllers import ErrorController

error_bp = Blueprint("error_bp", __name__)
error_controller = ErrorController()


@error_bp.route("/page-not-found")
def page_not_found():
    return error_controller.page_not_found()

@error_bp.route("/something-went-wrong")
def something_went_wrong():
    return error_controller.something_went_wrong()
