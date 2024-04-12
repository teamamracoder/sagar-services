from flask import Blueprint

from app.controllers import CouponController

coupon_bp = Blueprint("coupon_bp", __name__)
coupon_controller = CouponController()


@coupon_bp.route("/admin/coupons/")
def index():
    return coupon_controller.get()


@coupon_bp.route("/admin/coupons/data")
def get_coupon_data():
    return coupon_controller.get_coupon_data()




@coupon_bp.route("/admin/coupons/add/", methods=["GET", "POST"])
def add():
    return coupon_controller.create()



@coupon_bp.route("/admin/coupons/update/<int:id>", methods=["GET", "POST"])
def update(id):
    return coupon_controller.update(id)




@coupon_bp.route("/admin/coupons/status/<int:id>", methods=["GET"])
def status(id):
    return coupon_controller.status(id)

