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
        cart = self.cart_service.get_by_id(id)
        if cart is None:
            return {"status":"error","message":"item not found","data":None}
        is_active=self.cart_service.status(id)
        if is_active:
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
                    })
    
            return jsonify(response_data)
    
        except ValueError as e:
            return jsonify({'error': str(e)}), 500
        

    def create(self,product_id):
        logged_in_user,roles=get_current_user().values()
        if hasattr(logged_in_user, 'id'):
            cart_item = self.cart_service.get_cart_item_by_user_id_product_id(logged_in_user.id,product_id)
            try:
                if cart_item:
                    if cart_item.is_active:
                        self.status(cart_item.id)
                        return {"status":"success","message":"Product Removed From Cart","data":False}
                    else:
                        self.cart_service.update(
                            cart_item.id,
                            updated_by=logged_in_user.id,  
                            updated_at=datetime.now(),
                            status=1,
                            is_active = True
                        )
                        return {"status":"success","message":"Product Added to Cart","data":True}
                else:
                    self.cart_service.create(
                        created_by=logged_in_user.id,  
                        created_at=datetime.now(),
                        user_id=logged_in_user.id,
                        product_id=product_id,
                        status=1
                    )
                    return {"status":"success","message":"Product Added to Cart","data":True}

            except ValueError as e:
                return jsonify({'error': str(e)}), 500
            
        else:
            return {"status":"error","message":"Please <a href='/login'>log in</a>","data":False}

