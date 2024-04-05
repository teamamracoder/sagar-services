from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateCartForm
from app.services import CartService, ProductService
from datetime import datetime
from app.constants import cart_statuses
from app.auth import get_current_user

class CartController:
    def __init__(self) -> None:
        self.cart_service = CartService()
        self.product_service = ProductService()

    def get(self):
        return render_template("admin/cart/index.html")

    def get_cart_data(self):
        columns = ["id", "user_id", "product_id", "created_by", "created_at", "updated_by","updated_at","status", "is_active"]
        data = self.cart_service.get(request, columns)
        data = self.product_service.add_product_with_this(data)
        data = self.cart_service.add_status_with_cart(data)
        return jsonify(data)

    #admin creates cart
    def create(self):
        form = CreateCartForm()
        if form.validate_on_submit():
            self.cart_service.create(
                created_by=get_current_user().id,   #logged in user id
                created_at=datetime.now(),
                user_id=form.user_id.data,
                product_id=form.product_id.data,
                status=1
            )
            return redirect(url_for("cart.index"))
            # return render_template("admin/cart/add.html", form=form, error="cart already exists")
        return render_template("admin/cart/add.html", form=form)


    def cart_status(self, cart_id, status):
        cart = self.cart_service.get_by_id(cart_id)
        if cart is None:
            return render_template("admin/error/something_went_wrong.html")
        status_key=cart_statuses.get_key(status)

        is_active=True
        #update is_active = false if cart_status is not 'ADDED', it can be 'REMOVED' or 'ORDERED'
        if status_key is not 1:
            is_active=False
        self.cart_service.update(
            cart_id,
            updated_by=get_current_user().id,  
            updated_at=datetime.now(),
            status=status_key,
            is_active=is_active
        )
        return redirect(url_for("cart.index"))

    # is_active will be updated as activated/deactivated
    def status(self, id):
        cart = self.cart_service.get_by_id(id)
        if cart is None:
            return render_template("admin/error/something_went_wrong.html")
        self.cart_service.status(id)
        return redirect(url_for("cart.index"))

