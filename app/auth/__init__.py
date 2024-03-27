from flask_login import LoginManager, current_user, login_user, logout_user

from app.services import UserService

login_manager = LoginManager()
user_service = UserService()


def init_auth(app):
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"


# User loader function required by Flask-Login
@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return user_service.get_by_id(user_id)


def login(user):
    login_user(user)


def logout():
    logout_user()
