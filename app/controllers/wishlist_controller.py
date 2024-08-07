from flask import render_template, redirect, url_for, request, jsonify
from app.services import WishlistService, ProductService, CategoryService, CartService
from datetime import datetime
from app.auth import get_current_user

class WishlistController:
    def __init__(self) -> None:
        self.wishlist_service = WishlistService()
        self.product_service = ProductService()
        self.category_service = CategoryService()
        self.cart_service = CartService()

    def get(self):
        return render_template("admin/wishlist/index.html")

    def get_wishlist_data(self):
        columns = ["id", "user_id", "product_id", "created_by", "created_at", "is_active"]
        data = self.wishlist_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(data)
        return jsonify(combined_data)



    # is_active will be updated as activated/deactivated
    def status(self, wishlist_id):
        logged_in_user, roles = get_current_user().values()
        wishlist = self.wishlist_service.get_by_id(wishlist_id)
        if wishlist is None:
            return {"status":"error","message":"Wishlist Deactivated"}
        is_active=self.wishlist_service.status(wishlist_id)
        if is_active:
            return {"status":"success","message":"Wishlist Activated","data":is_active}
        wishlist_count = self.wishlist_service.get_total_wishlist_items_by_user_id(logged_in_user.id)
        return {"status":"success","message":"Wishlist Deactivated","data":is_active, "wishlist_count":wishlist_count}



    ## customer controllers ##

    def wishlist_page(self):
        return render_template("customer/wishlist.html")


    def wishlist_page_data(self):
        logged_in_user,roles=get_current_user().values()
        try:
            # Get wishlist items for the given user id
            wishlist_items = self.wishlist_service.get_wishlist_items_by_user_id(logged_in_user.id)

            # Extract product ids from wishlist items
            product_ids = [wishlist_item.product_id for wishlist_item in wishlist_items]

            # Get product details for the product ids
            products = self.product_service.get_product_details_by_ids(product_ids)
            # Construct response data
            response_data = []
            for wishlist_item in wishlist_items:
                product = next((product for product in products if product.id == wishlist_item.product_id), None)
                if product:
                    cart=self.cart_service.get_cart_item_by_user_id_product_id(logged_in_user.id,product.id)
                    in_cart=False
                    if cart:
                        if cart.is_active:
                            in_cart=True
                    response_data.append({
                        'id': wishlist_item.id,
                        'product_id': product.id,
                        'stock': product.stock,
                        'product_name': product.product_name,
                        'brand': product.brand,
                        'price': product.price,
                        'discount': product.discount,
                        'stock': product.stock,
                        'image': product.product_img_urls,
                        'in_cart':in_cart
                    })

            return jsonify(response_data)

        except ValueError as e:
            return jsonify({'error': str(e)}), 500


    def create(self,product_id):
        logged_in_user,roles=get_current_user().values()
        if hasattr(logged_in_user, 'id'):
            product=self.product_service.get_by_id(product_id)
            if product:
                wishlist_item=self.wishlist_service.get_wishlist_item_by_user_id_product_id(logged_in_user.id,product_id)
                if wishlist_item:
                    is_active=self.status(wishlist_item.id)
                    wishlist_count = self.wishlist_service.get_total_wishlist_items_by_user_id(logged_in_user.id)
                    if is_active['data']:
                        return {"status":"success","message":"Product Added To Wishlist","data":is_active['data'], "wishlist_count":wishlist_count}
                    return {"status":"success","message":"Product removed from Wishlist","data":is_active['data'], "wishlist_count":wishlist_count}

                else:
                    wishlist_item=self.wishlist_service.create(
                        created_by=logged_in_user.id,
                        created_at=datetime.now(),
                        user_id=logged_in_user.id,
                        product_id=product_id
                    )
                    wishlist_count = self.wishlist_service.get_total_wishlist_items_by_user_id(logged_in_user.id)
                    if wishlist_item:
                        return {"status":"success","message":"Product Added To Wishlist","data":wishlist_item.is_active,"wishlist_count":wishlist_count}
                    return {"status":"error","message":"Something went wrong"}
            else:
                return {"status":"error","message":"Something went wrong"}
        else:
            return {"status":"error","message":"Please <a href='/login'>log in</a>","data":False}