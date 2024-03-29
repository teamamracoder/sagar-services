from flask_login import LoginManager, current_user, login_user, logout_user
from functools import wraps
from flask import abort, redirect, url_for

from app.services import UserService

login_manager = LoginManager()
user_service = UserService()


def init_auth(app):
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"


def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))
            if not any(user_role.role in roles for user_role in current_user.roles):
                return redirect(url_for("error_bp.unauthorized_access"))
            return func(*args, **kwargs)

        return wrapper

    return decorator


# User loader function required by Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return user_service.get_by_id(user_id)


def login(user):
    login_user(user)


def logout():
    logout_user()
