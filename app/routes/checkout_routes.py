from flask import Blueprint
from app.controllers import CheckoutController
from flask_login import login_required
checkout_bp = Blueprint("checkout", __name__)
checkout_controller = CheckoutController()


@checkout_bp.route("/checkout/")
@login_required
def checkout_page():
    return checkout_controller.checkout_page()