from flask import render_template, redirect, url_for, request, jsonify
from app.services import ServiceService, ProductService, OrderService, BookingService, CouponService, UserService, OrderLogService, CartService
from datetime import datetime
from app.auth import get_current_user
from app.utils import cache


class CheckoutController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.product_service = ProductService()
        self.order_service = OrderService()
        self.booking_service = BookingService()
        self.coupon_service = CouponService()
        self.user_service = UserService()
        self.order_log_service = OrderLogService()
        self.cart_service = CartService()
    

    def checkout_page(self,product_id_param):
        if product_id_param !=0:
            product = self.product_service.get_by_id(product_id_param)
            if product:
                if product.stock<3:
                    return render_template("customer/cart.html")
            else:
                return render_template("customer/cart.html")
        
        logged_in_user,roles=get_current_user().values()
        cache_key = f"cart_{logged_in_user.id}"
        if product_id_param!=0:
            cache.set(cache_key, [{'product_id': product_id_param, 'quantity': 1}])
        product_ids = cache.get(cache_key)
        if product_ids:
            products = []
            for product_id in product_ids:
                item = self.product_service.get_by_id(product_id['product_id'])
                products.append(item)
            return render_template("customer/checkout.html",products=products, user=logged_in_user)
        else:
            return render_template("customer/cart.html")
    
    def update_quantity(self):
        logged_in_user, roles = get_current_user().values()
        try:
            # data = request.json
            product_id = request.form.get("product_id")
            quantity = request.form.get("qty")

            # Retrieve cart items from the cache
            cache_key = f"cart_{logged_in_user.id}"
            cart_items = cache.get(cache_key)

            # Initialize an empty list if cart_items is None
            if cart_items is None:
                cart_items = []


            # Filter out the item with the given product ID
            # cart_items = list(filter(lambda item: item['product_id'] != product_id, cart_items))
            cart_items = [cart_item for cart_item in cart_items if cart_item['product_id'] != int(product_id)]


            # Create a new dictionary with the updated quantity
            updated_item = {'product_id': int(product_id), 'quantity': int(quantity)}

            # Append the updated item to cart_items
            cart_items.append(updated_item)


            # Update the cache with the modified cart items
            cache.set(cache_key, cart_items)

            return {'status': 'success', 'message': 'Quantity updated successfully'}

        except Exception as e:
            print("Error:", e)
            return {'status': 'error', 'message': str(e)}


    def check_coupon(self):
        logged_in_user, roles = get_current_user().values()
        try:
            coupon_code = request.form.get("coupon_code")
            coupon = self.coupon_service.get_by_code(coupon_code)
            if coupon:
                is_valid_coupon = self.user_service.check_coupon_by_coupon_id(logged_in_user.id, coupon.id)
                if is_valid_coupon:
                    return {'status':'success','message': 'Valid coupon', 'type':coupon.discount_type, 'discount':coupon.discount}
                else:
                    return {'status':'error','message': 'Invalid coupon'}
            return {'status':'error','message': 'coupon not found'}


        except Exception as e:
            return {'status':'error','message': str(e)}

    def confirm(self):
        logged_in_user,roles=get_current_user().values()

        cache_key = f"cart_{logged_in_user.id}"
        products_with_qty = cache.get(cache_key)
        if products_with_qty:
            print(products_with_qty)

            products_info = []

            # Iterate through products_list
            for item in products_with_qty:
                product_id = item['product_id']
                qty = item['quantity']
                product = self.product_service.get_by_id(product_id)
                if product:
                    price = product.price
                    discount = product.discount
                    amount = calculate_amount(product_id, qty, price, discount)
                    item["price"]= amount  # Update the existing dictionary
                    products_info.append(item) 
                    order_amount = 0
                    if products_with_qty:
                        products = []
                        for product in products_with_qty:
                            item = self.product_service.get_by_id(product['product_id'])
                            products.append(item)

                        for product in products:
                            order_amount += (product.price - product.discount)

            pos = 0
            max_amount = 0
            count = 0
            for product in products_info:
                if max_amount<product['price']:
                    max_amount = product['price']
                    pos = count 
                count += 1

            coupon_code = request.form.get('coupon_code')
            if coupon_code != '':
                coupon = self.coupon_service.get_by_code(coupon_code)
                is_valid_coupon = self.user_service.check_coupon_by_coupon_id(logged_in_user.id, coupon.id)
                if is_valid_coupon:
                    discount = coupon.discount
                    if coupon.discount_type==1:
                        if (products_info[pos]['price'] - discount)<=0:
                            order_amount=0
                        else:
                            products_info[pos]['price']=products_info[pos]['price'] - discount
                            # order_amount -= discount
                    else:
                        if (order_amount - (order_amount*(discount/100)))<=0:
                            products_info[pos]['price']=0
                        else:
                            products_info[pos]['price'] -= products_info[pos]['price']*(discount/100)
                    
                    self.user_service.delete_coupon(logged_in_user.id, coupon.id)

            is_new_address = request.form.get('new-address')
            
            if is_new_address:
                shipping_address = request.form.get("StreetAddress")+","+request.form.get("Landmark")+","+request.form.get("Additional Address")+","+request.form.get("City")+","+request.form.get("State")
                area_pincode=request.form.get("PinCode")
                mobile = request.form.get("MobileNo")
            else:
                mobile = logged_in_user.mobile
                shipping_address = logged_in_user.address
                area_pincode = logged_in_user.pincode
            if request.form.get("pay-method")=='1':
                payment_status = 2
            else:
                payment_status = 1
            print(payment_status)

            for order_details in products_info:
                order_details.update({"delivery_charge": 50,
                "created_by":logged_in_user.id,
                "created_at":datetime.now(),
                "user_id":logged_in_user.id,
                "payment_method":request.form.get("pay-method"),
                "order_status":1,
                "area_pincode":area_pincode,
                "shipping_address":shipping_address,
                "mobile":mobile,
                "payment_status":payment_status,
                })
            

            for order_details in products_info:
                order = self.order_service.create(**order_details)
                print(order.id)
                self.order_log_service.create(
                    created_by=logged_in_user.id,
                    created_at=datetime.now(),
                    order_id=order.id,
                    order_status=order.order_status
                )
                self.cart_service.update_cart_status(logged_in_user.id,product_id,2)

            cache.delete(f"cart_{logged_in_user.id}")
            return "order success"
        return render_template("customer/cart.html")




def calculate_amount(product_id, qty, price, discount):
    amount = (price - discount) * qty
    return amount