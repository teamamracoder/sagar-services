# from flask import render_template, redirect, url_for
# from app.forms import CreateCouponForm
# from app.services import CouponService

# coupon_service = CouponService()


# class CouponController:

#     def create(self):
        
#         form = CreateCouponForm()
#         if form.validate_on_submit():
#             coupon_service.create(
#                 # created_by=form.created_by.data,
#                 # updated_by=form.updated_by.data,
#                 coupon_code=form.coupon_code.data,
#                 expiry_date=form.expiry_date.data,
#                 discount_type=form.discount_type.data,
#                 discount=form.discount.data,
#                 coupon_img_url=form.coupon_img_url.data,
#                 count=form.count.data
#             )
#             return redirect(url_for("coupon_bp.index"))
#         return render_template("admin/coupon/add.html", form=form)
        
  


        
#     def get(self):
#         coupons = coupon_service.get()
#         return render_template("admin/coupon/index.html", coupons=coupons)






import os
from flask import render_template, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from app.forms import CreateCouponForm
from app.services import CouponService

coupon_service = CouponService()

class CouponController:
    def create(self):
        form = CreateCouponForm()
        if form.validate_on_submit():
            # Store the image file in the 'image' folder
            image_file = form.coupon_img_url.data
            if image_file:
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(current_app.root_path, 'static', 'img', filename)
                image_file.save(image_path)
                
            # Create the coupon with the image file path
            coupon_service.create(
                coupon_code=form.coupon_code.data,
                expiry_date=form.expiry_date.data,
                discount_type=form.discount_type.data,
                discount=form.discount.data,
                coupon_img_url=os.path.join('img', filename) if image_file else None,
                count=form.count.data
            )
            return redirect(url_for("coupon_bp.index"))
        return render_template("admin/coupon/add.html", form=form)
    
    def get(self):
        coupons = coupon_service.get()
        return render_template("admin/coupon/index.html", coupons=coupons)
