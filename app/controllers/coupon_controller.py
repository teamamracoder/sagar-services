from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateCouponForm, UpdateCouponForm
from app.services import CouponService


class CouponController:

    def __init__(self) -> None:
        self.coupon_service= CouponService()

    def create(self):
        
        form = CreateCouponForm()
        if form.validate_on_submit():
            self.coupon_service.create(
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
        # coupons = self.coupon_service.get()
        return render_template("admin/coupon/index.html")


    def get_coupon_data(self):
        # Determine the column to sort by
        columns = ["id", "coupon_code", "expiry_date", "discount"]
        data = self.coupon_service.get(request, columns)
        # Create a dictionary containing the sorted data
       
        # Return the sorted data in JSON format
        return jsonify(data)
    


    def update(self,id):
        coupon = self.coupon_service.get_by_id(id)
        form = UpdateCouponForm(obj=coupon)
        if form.validate_on_submit():
            self.coupon_service.update(
                id=id,
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
        return render_template("admin/coupon/update.html", id=id, form=form)



    def status(self,id):
        coupon = self.coupon_service.get_by_id(id)
        if coupon is None:
            return render_template("admin/error/something_went_wrong.html")
        self.coupon_service.status(id)
        return redirect(url_for("coupon_bp.index"))