from flask import render_template, redirect, url_for
from app.forms import CreateCouponForm
from app.services import CouponService

coupon_service = CouponService()


class CouponController:

    def create(self):
        
        form = CreateCouponForm()
        if form.validate_on_submit():
            coupon_service.create(
                # created_by=form.created_by.data,
                # updated_by=form.updated_by.data,
                coupon_code=form.coupon_code.data,
                expiry_date=form.expiry_date.data,
                discount_type=form.discount_type.data,
                discount=form.discount.data,
                coupon_img_url=form.coupon_img_url.data,
                count=form.count.data
            )
            return redirect(url_for("coupon_bp.index"))
        return render_template("admin/coupon/add.html", form=form)
        
  


        
    def get(self):
        coupons = coupon_service.get()
        return render_template("admin/coupon/index.html", coupons=coupons)
