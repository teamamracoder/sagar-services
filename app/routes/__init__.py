from .auth_routes import auth_bp
from .error_routes import error_bp
from .user_routes import user_bp
from .role_routes import role_bp
from .home_routes import home_bp
from .category_routes import category_bp
from .product_routes import product_bp
from .dashboard_routes import dashboard_bp
from .converastion_routes import conversation_bp
from .message_routes import message_bp
from .product_qna_routes import product_qna_bp
from .cart_routes import cart_bp
from .wishlist_routes import wishlist_bp
from .product_review_routes import product_review_bp
from .order_routes import order_bp
from .service_routes import service_bp
from .service_type_routes import service_type_bp
from .service_answer_routes import service_answer_bp
from .service_question_routes import service_question_bp

# register blueprints
blueprints = [auth_bp, error_bp, user_bp, role_bp, home_bp, category_bp, product_bp, dashboard_bp, service_bp, service_type_bp, service_answer_bp, service_question_bp,product_qna_bp, cart_bp, wishlist_bp, product_review_bp, order_bp, conversation_bp, message_bp]

def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
