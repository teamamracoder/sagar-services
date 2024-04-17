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
        logged_in_user,roles=get_current_user().values()
        form = CreateCartForm()
        if form.validate_on_submit():
            self.cart_service.create(
                created_by=logged_in_user.id,   #logged in user id
                created_at=datetime.now(),
                user_id=logged_in_user.id,
                product_id=form.product_id.data,
                status=1
            )
            return redirect(url_for("cart.index"))
            # return render_template("admin/cart/add.html", form=form, error="cart already exists")
        return render_template("admin/cart/add.html", form=form)


    def cart_status(self, cart_id, status):
        logged_in_user,roles=get_current_user().values()
        cart = self.cart_service.get_by_id(cart_id)
        if cart is None:
            return {"status":"error","message":"Cart Not Found"}
        status_key=cart_statuses.get_key(status)

        is_active=True
        #update is_active = false if cart_status is not 'ADDED', it can be 'REMOVED' or 'ORDERED'
        if status_key != 1:
            is_active=False
        self.cart_service.update(
            cart_id,
            updated_by=logged_in_user.id,  
            updated_at=datetime.now(),
            status=status_key,
            is_active=is_active
        )
        return {"status":"success","message":f"Cart Status Changed to {status}","data":status}

    # is_active will be updated as activated/deactivated
    def status(self, id):
        logged_in_user,roles=get_current_user().values()
        cart = self.cart_service.get_by_id(id)
        if cart is None:
            return {"status":"error","message":"Cart Not Found"}
        is_active=self.cart_service.status(id)
        if is_active:
            self.cart_service.update(
                cart.id,
                updated_by=logged_in_user.id,  
                updated_at=datetime.now(),
                status=1
            )
            return {"status":"success","message":"Cart Activated","data":is_active}
        return {"status":"success","message":"Cart Deactivated","data":is_active}



## customer controllers ##

    def cart_page(self):
        return render_template("customer/cart.html")
    
    def cart_page_data(self):
        logged_in_user,roles=get_current_user().values()
        try:
            # Get cart items for the given user id
            cart_items = self.cart_service.get_cart_items_by_user_id(logged_in_user.id)
    
            # Extract product ids from cart items
            product_ids = [cart_item.product_id for cart_item in cart_items]
    
            # Get product details for the product ids
            products = self.product_service.get_product_details_by_ids(product_ids)
    
            # Construct response data
            response_data = []
            for cart_item in cart_items:
                product = next((product for product in products if product.id == cart_item.product_id), None)
                if product:
                    response_data.append({
                        'id': cart_item.id,
                        'product_id':product.id,
                        'product_name': product.product_name,
                        'model': product.model,
                        'price': product.price,
                        'discount': product.discount,
                        'stock': product.stock,
                        'image': product.product_img_urls
                        # Add more product details as needed
                    })
    
            return jsonify(response_data)
    
        except ValueError as e:
            return jsonify({'error': str(e)}), 500
        

    def add_to_cart(self,product_id):
        logged_in_user,roles=get_current_user().values()
        cart_item = self.cart_service.get_cart_item_user_id_product_id()
        try:
            if cart_item:
                if cart_item.is_active:
                    return {"status":"error","message":"Already In Cart","data":False}
                else:
                    self.cart_service.update(
                        cart_item.id,
                        updated_by=logged_in_user.id,  
                        updated_at=datetime.now(),
                        status=1,
                        is_active = True
                    )
                    return {"status":"error","message":"Product Added to Cart","data":True}
            else:
                self.cart_service.create(
                    created_by=logged_in_user.id,   #logged in user id
                    created_at=datetime.now(),
                    user_id=logged_in_user.id,
                    product_id=product_id,
                    status=1
                )
                return {"status":"success","message":"Cart Activated","data":True}

        except ValueError as e:
            return jsonify({'error': str(e)}), 500

