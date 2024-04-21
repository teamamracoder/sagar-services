from flask import Blueprint

from app.controllers import AuthController

auth_bp = Blueprint("auth", __name__)
auth_controller = AuthController()


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return auth_controller.login()


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    return auth_controller.signup()


@auth_bp.route("/reset-password")
def reset_password():
    return auth_controller.reset_password()


@auth_bp.route("/verify-otp/<int:id>", methods=["GET", "POST"])
def verify_otp(id):
    return auth_controller.verify_otp(id)


@auth_bp.route("/logout")
def logout():
    return auth_controller.logout()
