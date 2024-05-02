from flask import Blueprint
from app.controllers import CouponController
from app.constants import roles
from app.auth import role_required
from flask_login import login_required

coupon_bp = Blueprint("coupon", __name__)
coupon_controller = CouponController()


@coupon_bp.route("/admin/coupons/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return coupon_controller.get()


@coupon_bp.route("/admin/coupons/data")
def get_coupon_data():
    return coupon_controller.get_coupon_data()




@coupon_bp.route("/admin/coupons/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return coupon_controller.create()



@coupon_bp.route("/admin/coupons/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return coupon_controller.update(id)




@coupon_bp.route("/admin/coupons/status/<int:id>", methods=["GET"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return coupon_controller.status(id)

@coupon_bp.route("/admin/coupons/send_coupon/<int:id>/<string:user_id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def send_coupon(id,user_id):
    return coupon_controller.send_coupon(id,user_id)

