from flask import render_template, redirect, url_for, request, jsonify
# from app.forms import CreateWishlistForm
from app.services import ServiceService, ProductService, OrderService, BookingService
from datetime import datetime
from app.auth import get_current_user

class CheckoutController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.product_service = ProductService()
        self.order_service = OrderService()
        self.booking_service = BookingService()
    
    
    def checkout_page(self,product_id):
        logged_in_user,roles=get_current_user().values()
        product = self.product_service.get_by_id(product_id)
        if product:
            return render_template("customer/checkout.html", product_id=product_id)
        return render_template("error/page_not_found.html")
