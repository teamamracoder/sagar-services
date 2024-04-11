from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateWishlistForm
from app.services import WishlistService, ProductService
from datetime import datetime
from app.auth import get_current_user

class WishlistController:
    def __init__(self) -> None:
        self.wishlist_service = WishlistService()
        self.product_service = ProductService()

    def get(self):
        return render_template("admin/wishlist/index.html")

    def get_wishlist_data(self):
        columns = ["id", "user_id", "product_id", "created_by", "created_at", "is_active"]
        data = self.wishlist_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(data)
        return jsonify(combined_data)

    #admin creates wishlist
    def create(self):
        form = CreateWishlistForm()
        if form.validate_on_submit():
            self.wishlist_service.create(
                created_by=get_current_user().id,   #logged in user id
                created_at=datetime.now(),
                user_id=form.user_id.data,
                product_id=form.product_id.data
            )
            return redirect(url_for("wishlist.index"))
            # return render_template("admin/wishlist/add.html", form=form, error="wishlist already exists")
        return render_template("admin/wishlist/add.html", form=form)

    # is_active will be updated as activated/deactivated
    def status(self, wishlist_id):
        wishlist = self.wishlist_service.get_by_id(wishlist_id)
        if wishlist is None:
            return render_template("admin/error/something_went_wrong.html")
        is_active=self.wishlist_service.status(wishlist_id)
        if is_active:
            return {"status":"success","message":"Category Activated","data":is_active}
        return {"status":"success","message":"Category Deactivated","data":is_active}