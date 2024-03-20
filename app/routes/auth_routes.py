from flask import Blueprint

from app.controllers import AuthController

auth_bp = Blueprint("auth_bp", __name__)
auth_controller = AuthController()


@auth_bp.route("/login")
def login():
    return auth_controller.login()

@auth_bp.route("/signup")
def signup():
    return auth_controller.signup()

@auth_bp.route("/reset-password")
def reset_password():
    return auth_controller.reset_password()
