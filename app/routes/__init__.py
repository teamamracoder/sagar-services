from .auth_routes import auth_bp
from .error_routes import error_bp
from .user_routes import user_bp
from .role_routes import role_bp
from .home_routes import home_bp
from .category_routes import category_bp
from .product_routes import product_bp
from .dashboard_routes import dashboard_bp
from .coupon_routes import coupon_bp

# register blueprints
blueprints = [auth_bp, error_bp, user_bp, role_bp, home_bp, category_bp, product_bp, dashboard_bp, coupon_bp]


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
