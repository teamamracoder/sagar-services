from flask import Blueprint

from app.controllers import CouponController

coupon_bp = Blueprint("coupon_bp", __name__)
coupon_controller = CouponController()


@coupon_bp.route("/admin/coupons/")
def index():
    return coupon_controller.get()


@coupon_bp.route("/admin/coupons/add/", methods=["GET", "POST"])
def add():
    return coupon_controller.create()
