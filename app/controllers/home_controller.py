from flask import render_template
from app.services import ProductService
from app.services import CategoryService
from app.services import ServiceService,OrderService,ProductReviewService,CartService,WishlistService,ServiceReviewService,UserService
from app.auth import get_current_user
from flask import jsonify

class HomeController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.category_service = CategoryService()
        self.service_service = ServiceService()
        self.order_service=OrderService()
        self.product_reviews_service=ProductReviewService()
        self.service_reviews_service=ServiceReviewService()
        self.cart_service=CartService()
        self.wish_service=WishlistService()
        self.user_service=UserService()


    def homepage(self):
        products=self.product_service.get_active()
        latest_products=self.product_service.get_latest_products()
        product_services=self.service_service.get_active()
        categories=self.category_service.get_active()

        top_10_orders=self.order_service.get_top_10_ordered_products()
        top_10_product_ids = [order.id for order in top_10_orders]
        top_10_products =self.product_service.get_product_details_by_ids(top_10_product_ids)
        top_10_products.reverse()
        product_reviews=self.product_reviews_service.get_review_by_product_ids(top_10_product_ids)

    #    For BestSelling
        bestselling_products=[]
        for product in top_10_products:
            serialized_bestselling_products = self.product_service.serialized_products(product)
            bestselling_products.append(serialized_bestselling_products)
        bestselling_products=self.product_reviews_service.get_reviews_by_product_for_home(bestselling_products)
        monitor_products = []
        laptop_products = []
        for category in categories:
           products = self.product_service.get_products_by_category(category.id)
           monitor_products_in_category = [product for product in products if category.category_name.lower() == "monitor"]
           monitor_products.extend(monitor_products_in_category)

           laptop_products_in_category = [product for product in products if category.category_name.lower() == "laptop"]
           laptop_products.extend(laptop_products_in_category)

        # For monitor_products
        for_monitor_products=[]
        for product in monitor_products:
            serialized_monitor_products = self.product_service.serialized_products(product)
            for_monitor_products.append(serialized_monitor_products)
        for_monitor_products=self.product_reviews_service.get_reviews_by_product_for_home(for_monitor_products)

        # For monitor_products
        for_laptop_products=[]
        for product in laptop_products:
            serialized_laptop_products = self.product_service.serialized_products(product)
            for_laptop_products.append(serialized_laptop_products)
        for_laptop_products=self.product_reviews_service.get_reviews_by_product_for_home(for_laptop_products)


        # For service
        for_product_services=[]
        for service in product_services:
            serialized_product_services = self.service_service.serialized_product_services(service)
            for_product_services.append(serialized_product_services)

        for_product_services=self.service_reviews_service.get_reviews_by_service_for_home (for_product_services)

        for_product_services=self.user_service.get_user_by_reviews_for_home(for_product_services)


        data = {
    "products": {
            "all_products": products,
            "latest_products": latest_products,
            "product_reviews":product_reviews,
            "top_10_products":bestselling_products,
            "monitor_products":for_monitor_products,
            "laptop_products":for_laptop_products
        },
        "services": for_product_services,
        "categories": categories

}

        return render_template("customer/home.html",data=data)

    # Get Total Cart and Wish of User
    def get_total_cart_and_wish(self):
        logged_in_user, roles = get_current_user().values()
        try:
            totalCart = self.cart_service.get_total_cart_items_by_user_id(logged_in_user.id)
            totalWish = self.wish_service.get_total_wishlist_items_by_user_id(logged_in_user.id)
            user_data=self.user_service.get_user_by_id(logged_in_user.id)
            user_profile_photo_url=user_data[0].profile_photo_url
            if totalCart is not None or totalWish is not None:
                total_cart_and_wish = {
                    "status": "success",
                    "message": "Data retrieved successfully",
                    "data": {
                        "totalCart": totalCart,
                        "totalWish": totalWish
                    },
                    "user_profile_photo_url":user_profile_photo_url
                }
                return jsonify(total_cart_and_wish)
            else:
                return {"status":"success","message":"write a message"}

        except Exception as e:
            return {"status":"failed","message":"something went wrong"}
