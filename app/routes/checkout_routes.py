from flask import Blueprint
from app.controllers import CheckoutController
from flask_login import login_required
checkout_bp = Blueprint("checkout", __name__)
checkout_controller = CheckoutController()


@checkout_bp.route("/checkout/<int:product_id>")
@login_required
def checkout_page(product_id):
    return checkout_controller.checkout_page(product_id)

@checkout_bp.route("/checkout/qty", methods=["GET","POST"])
@login_required
def update_quantity():
    return checkout_controller.update_quantity()

@checkout_bp.route("/checkout/check", methods=["GET","POST"])
@login_required
def check_coupon():
    return checkout_controller.check_coupon()


@checkout_bp.route("/confirm", methods=["GET","POST"])
@login_required
def confirm():
    return checkout_controller.confirm()