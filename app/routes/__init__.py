from .auth_routes import auth_bp
from .error_routes import error_bp
from .user_routes import user_bp
from .role_routes import role_bp
from .home_routes import home_bp
from .category_routes import category_bp
from .service_routes import service
from .service_type_routes import service_type
from .service_question_routes import service_question
from .service_answer_routes import service_answer

# register blueprints
blueprints = [auth_bp, error_bp, user_bp, role_bp, home_bp, category_bp, service, service_type, service_question, service_answer]


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
