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



    # is_active will be updated as activated/deactivated
    def status(self, wishlist_id):
        wishlist = self.wishlist_service.get_by_id(wishlist_id)
        if wishlist is None:
            return {"status":"error","message":"Wishlist Deactivated"}
        is_active=self.wishlist_service.status(wishlist_id)
        if is_active:
            return {"status":"success","message":"Wishlist Activated","data":is_active}
        return {"status":"success","message":"Wishlist Deactivated","data":is_active}
    


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
                    response_data.append({
                        'id': wishlist_item.id,
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
        product=self.product_service.get_by_id(product_id)
        if product:
            wishlist_item=self.wishlist_service.get_wishlist_item_by_user_id_product_id(logged_in_user.id,product_id)
            if wishlist_item:
                is_active=self.status(wishlist_item.id)
                if is_active['data']:
                    return {"status":"success","message":"Product Added To Wishlist","data":is_active['data']}
                return {"status":"success","message":"Product removed from Wishlist","data":is_active['data']}
            
            else:
                wishlist_item=self.wishlist_service.create(
                    created_by=logged_in_user.id,
                    created_at=datetime.now(),
                    user_id=logged_in_user.id,
                    product_id=product_id
                )
                if wishlist_item:
                    return {"status":"success","message":"Product Added To Wishlist","data":wishlist_item.is_active}
                return {"status":"error","message":"Something went wrong"}

        else:
            return {"status":"error","message":"Something went wrong"}