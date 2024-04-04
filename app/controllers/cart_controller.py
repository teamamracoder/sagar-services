from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateCartForm
from app.services import CartService, ProductService
from datetime import datetime
from app.constants import cart_statuses

class CartController:
    def __init__(self) -> None:
        self.cart_service = CartService()
        self.product_service = ProductService()

    def get(self):
        return render_template("admin/cart/index.html")

    def get_cart_data(self):
        columns = ["id", "user", "product_id", "created_by", "created_at", "updated_by","updated_at","status", "is_active"]
        data = self.cart_service.get(request, columns)
        product_combined_data = self.product_service.add_product_with_this(data)
        status_combined_data = self.cart_service.add_status_with_cart(product_combined_data)
        return jsonify(status_combined_data)

    #admin creates cart
    def create(self):
        form = CreateCartForm()
        if form.validate_on_submit():
            self.cart_service.create(
                created_by=1,   #logged in user id
                created_at=datetime.now(),
                user_id=form.user_id.data,
                product_id=form.product_id.data,
                status=3
            )
            return redirect(url_for("cart.index"))
            # return render_template("admin/cart/add.html", form=form, error="cart already exists")
        return render_template("admin/cart/add.html", form=form)

    # customer's add to cart
    def add_to_cart(self,product_id):
        self.cart_service.create(
            created_by=1,   #logged in user id
            created_at=datetime.now(),
            user_id=1,    # logged in user id
            product_id=product_id,
            status=3
        )

    # status will be true when added to cart, false when product ordered

    def cart_status(self, cart_id, status):
        cart = self.cart_service.get_by_id(cart_id)
        if cart is None:
            return render_template("admin/error/something_went_wrong.html")
        status_key=cart_statuses.get_key(status)
        self.cart_service.update(
            cart_id,
            updated_by=1,   #logged in user
            updated_at=datetime.now(),
            status=status_key
        )
        return redirect(url_for("cart.index"))

    # is_active will be updated as activated/deactivated
    def status(self, id):
        cart = self.cart_service.get_by_id(id)
        if cart is None:
            return render_template("admin/error/something_went_wrong.html")
        self.cart_service.status(id)
        return redirect(url_for("cart.index"))

