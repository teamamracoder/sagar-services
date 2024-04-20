from flask_login import LoginManager, current_user, login_user, logout_user
from functools import wraps
from flask import abort, redirect, url_for
from app.services import RoleService
from app.services import UserService

login_manager = LoginManager()
user_service = UserService()
role_service = RoleService()

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



def get_current_user():
    try:
        if current_user.id:
            roles=role_service.get_roles_by_user_id_list(user_id=current_user.id)
            return {'logged_in_user':current_user,'roles':roles}
        
    except Exception as e:
        return {'logged_in_user':current_user,'roles':[]}