from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateCouponForm, UpdateCouponForm
from app.services import CouponService
from app.auth import get_current_user
from datetime import datetime
from app.constants import discount_types

class CouponController:

    def __init__(self) -> None:
        self.coupon_service= CouponService()

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateCouponForm()
        form.discount_type.choices = discount_types.get_all_items()
        if form.validate_on_submit():
            self.coupon_service.create(
                created_at=datetime.now(),
                created_by=logged_in_user.id,
                coupon_code=form.coupon_code.data,
                expiry_date=form.expiry_date.data,
                discount_type=form.discount_type.data,
                discount=form.discount.data,
                coupon_img_url=form.coupon_img_url.data,
                count=form.count.data
            )
            return redirect(url_for("coupon.index"))
        return render_template("admin/coupon/add.html", form=form)
        
  
    def get(self):
        return render_template("admin/coupon/index.html")


    def get_coupon_data(self):
        # Determine the column to sort by
        columns = ["id", "coupon_code", "expiry_date", "discount", "discount_type", "count"]
        # Create a dictionary containing the sorted data
        data = self.coupon_service.get(request, columns)
        data = self.coupon_service.add_discount_type_with_this(data)
        # Return the sorted data in JSON format
        return jsonify(data)
    


    def update(self,id):
        logged_in_user,roles=get_current_user().values()
        coupon = self.coupon_service.get_by_id(id)
        form = UpdateCouponForm(obj=coupon)
        form.discount_type.choices = discount_types.get_all_items()
        if form.validate_on_submit():
            self.coupon_service.update(
                id=id,
                updated_by=logged_in_user.id,
                updated_at=datetime.now(),
                coupon_code=form.coupon_code.data,
                expiry_date=form.expiry_date.data,
                discount_type=form.discount_type.data,
                discount=form.discount.data,
                coupon_img_url=form.coupon_img_url.data,
                count=form.count.data
            )
            return redirect(url_for("coupon.index"))
        return render_template("admin/coupon/update.html", id=id, form=form)



    def status(self,id):
        coupon = self.coupon_service.get_by_id(id)
        if coupon is None:
            return {"status":"error","message":"item not found","data":None}
        is_active=self.coupon_service.status(id)
        if is_active:
            return {"status":"success","message":"Category Activated","data":is_active}
        return {"status":"success","message":"Category Deactivated","data":is_active}