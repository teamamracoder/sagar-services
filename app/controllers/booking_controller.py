from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateBookingForm,UpdateBookingForm
from app.services import ServiceService
from app.services import BookingService
from datetime import datetime
from app.constants import payment_methods
from app.constants import booking_statuses
from app.constants import payment_statuses
from app.services import UserService
from app.auth import get_current_user

class BookingController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.booking_service = BookingService()
        self.user_service = UserService()

    def get(self):
        return render_template("admin/booking/index.html")

    def get_booking_data(self):
        columns = ["id", "created_by", "created_at","updated_by","updated_at","is_active","service_id","user_id","staff_id","total_charges","service_location","service_status","payment_status","payment_method","area_pincode"]
        data = self.booking_service.get(request, columns)
        data = self.service_service.add_service_with_this(data)
        data = self.user_service.add_user_with_this(data)
        data = self.booking_service.add_payment_method_with_this(data)
        data = self.booking_service.add_booking_status_with_this(data)
        data = self.booking_service.add_payment_status_with_this(data)
        return jsonify(data)

    def create(self):
        form = CreateBookingForm()
        form.payment_method.choices = payment_methods.get_all_items()
        form.booking_status.choices = booking_statuses.get_all_items()
        form.payment_status.choices = payment_statuses.get_all_items()
     
        if form.validate_on_submit():
            if self.booking_service.create(
                created_by=1,
                created_at=datetime.now(),
                service_id=form.service_id.data,
                user_id=form.user_id.data,
                quantity=form.quantity.data,
                price=form.price.data,
                payment_method=form.payment_method.data,
                booking_status=form.booking_status.data,
                shipping_address=form.shipping_address.data,
                payment_status=form.payment_status.data,
                area_pincode=form.area_pincode.data,
            ):
                return redirect(url_for("booking.index"))
        return render_template("admin/booking/add.html", form=form)

    def update(self, id):
        booking = self.booking_service.get_by_id(id)
        if booking is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateBookingForm(obj=booking)

        service = self.service_service.get_by_id(booking.service_id)
        form.service_id.choices = [(service.id, service.service_name)]

        form.payment_method.choices = payment_methods.get_all_items()
        form.booking_status.choices = booking_statuses.get_all_items()
        form.payment_status.choices = payment_statuses.get_all_items()
        if form.validate_on_submit():
            updated_data = {
                'service_id': form.service_id.data,
                'user_id': form.user_id.data,
                'quantity': form.quantity.data,
                'price': form.price.data,
                'payment_method': form.payment_method.data,
                'booking_status': form.booking_status.data,
                'shipping_address': form.shipping_address.data,
                'payment_status': form.payment_status.data,
                'area_pincode': form.area_pincode.data,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
            self.booking_service.update(id, **updated_data)
            return redirect(url_for("booking.index"))
        
        return render_template("admin/booking/update.html", id=id, form=form)

    def status(self, id):
        booking = self.booking_service.get_by_id(id)
        if booking is None:
            return render_template("admin/error/something_went_wrong.html")
        self.booking_service.status(id)
        return redirect(url_for("booking.index"))

    def booking_status(self,id,status_type,status):
        booking = self.booking_service.get_by_id(id)
        if booking is None:
            return render_template("admin/error/something_went_wrong.html")
        if status_type == 'payment':
            status_key = payment_statuses.get_key(status)
            updated_data = {
                'payment_status': status_key,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
        if status_type == 'booking':
            status_key = booking_statuses.get_key(status)
            updated_data = {
                'booking_status': status_key,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
        self.booking_service.update(id, **updated_data)
        return redirect(url_for("booking.index"))
