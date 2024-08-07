from flask import Blueprint

from app.controllers import ErrorController

error_bp = Blueprint("error_bp", __name__)
error_controller = ErrorController()


@error_bp.route("/<path:path>")
def page_not_found(path):
    return error_controller.page_not_found()


@error_bp.route("/something-went-wrong")
def something_went_wrong():
    return error_controller.something_went_wrong()


@error_bp.route("/unauthorized-access")
def unauthorized_access():
    return error_controller.unauthorized_access()

@error_bp.route("/deactivated")
def deactivated():
    return error_controller.deactivated()
