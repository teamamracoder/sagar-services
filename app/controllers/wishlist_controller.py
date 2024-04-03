from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateWishlistForm
from app.services import WishlistService, ProductService
from datetime import datetime


class WishlistController:
    def __init__(self) -> None:
        self.wishlist_service = WishlistService()
        self.product_service = ProductService()

    def get(self):
        return render_template("admin/wishlist/index.html")

    def get_wishlist_data(self):
        columns = ["id", "user", "product_id", "created_by", "created_at", "is_active"]
        data = self.wishlist_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(data)
        return jsonify(combined_data)

    #admin creates wishlist
    def create(self):
        form = CreateWishlistForm()
        if form.validate_on_submit():
            self.wishlist_service.create(
                created_by=1,   #logged in user id
                created_at=datetime.now(),
                user_id=form.user_id.data,
                product_id=form.product_id.data
            )
            return redirect(url_for("wishlist.index"))
            # return render_template("admin/wishlist/add.html", form=form, error="wishlist already exists")
        return render_template("admin/wishlist/add.html", form=form)

    # customer's add to wishlist
    def add_to_wishlist(self,product_id):
        self.wishlist_service.create(
            created_by=1,   #logged in user id
            created_at=datetime.now(),
            user_id=1,    # logged in user id
            product_id=product_id
        )

    # is_active will be updated as activated/deactivated
    def status(self, wishlist_id):
        wishlist = self.wishlist_service.get_by_id(wishlist_id)
        if wishlist is None:
            return render_template("admin/error/something_went_wrong.html")
        self.wishlist_service.status(wishlist_id)
        return redirect(url_for("wishlist.index"))