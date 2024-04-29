from flask import render_template, redirect, url_for, request, jsonify
from app.auth import get_current_user
from app.services import UserService,OrderService,ProductService,BookingService,ProductReviewService,ServiceService

class DashboardController:

    def __init__(self) -> None:
        self.product_service = ProductService()
        self.order_service=OrderService()
        self.user_service=UserService()
        self.booking_service=BookingService()
        self.product_rating_service=ProductReviewService()
        self.service_service=ServiceService()

    def dashboard(self):
        return render_template("admin/dashboard.html", user=get_current_user())


    def get_chart_data(self):
        range = request.form.get("range")
        user_data=self.user_service.get_users_registered_data_for_Chart(range)
        order_data=self.order_service.get_ordered_data_for_Chart(range)
        order_status=self.order_service.get_order_statuses_count(range)
        service_status=self.booking_service.get_booking_statuses_count(range)
        product_rating=self.product_rating_service.get_product_rating_counts(range)
        total_user=self.user_service.get_all_users(range)
        total_order=self.order_service.get_all_orders(range)
        total_product=self.product_service.get_all_products(range)
        total_service=self.service_service.get_all_services(range)
        print(user_data)
        dataset = {
            "dataset1": user_data,
            "dataset2": order_data,
            "dataset3": order_status,
            "dataset4": service_status,
            "dataset5": product_rating,
            "total_user":total_user,
            "total_order":total_order,
            "total_product":total_product,
            "total_service":total_service

        }
        return jsonify(dataset)





