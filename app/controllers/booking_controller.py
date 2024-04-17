from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateBookingForm,UpdateBookingForm
from app.services import ServiceService
from app.services import BookingService
from datetime import datetime
from app.constants import payment_methods
from app.constants import service_statuses
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
        data = self.booking_service.add_service_status_with_this(data)
        data = self.booking_service.add_payment_status_with_this(data)
        return jsonify(data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateBookingForm()
        services=self.service_service.get_active()
        form.service_id.choices = [(service.id, service.service_name) for service in services]
       
        form.payment_method.choices = payment_methods.get_all_items()
        form.service_status.choices = service_statuses.get_all_items()
        form.payment_status.choices = payment_statuses.get_all_items()
     
        if form.validate_on_submit():
            if self.booking_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                service_id=form.service_id.data,
                user_id=get_current_user().id,
                total_charges=form.total_charges.data,
                service_location=form.service_location.data,
                service_status=form.service_status.data,
                payment_status=form.payment_status.data,
                payment_method=form.payment_method.data,
                area_pincode=form.area_pincode.data,
                ):
                return redirect(url_for("booking.index"))
        return render_template("admin/booking/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        booking = self.booking_service.get_by_id(id)
        if booking is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateBookingForm(obj=booking)

        service = self.service_service.get_by_id(booking.service_id)
        form.service_id.choices = [(service.id, service.service_name)]

        form.payment_method.choices = payment_methods.get_all_items()
        form.service_status.choices = service_statuses.get_all_items()
        form.payment_status.choices = payment_statuses.get_all_items()
        if form.validate_on_submit():
            if self.booking_service.update(
                id=id,
                updated_by=logged_in_user.id,
                updated_at=datetime.now(),
                service_id=form.service_id.data,
                user_id=logged_in_user.id,
                staff_id=form.staff_id.data,
                total_charges=form.total_charges.data,
                service_location=form.service_location.data,
                service_status=form.service_status.data,
                payment_status=form.payment_status.data,
                payment_method=form.payment_method.data,
                area_pincode=form.area_pincode.data
                ):
                return redirect(url_for("booking.index"))
        return render_template("admin/booking/update.html", id=id, form=form)

    def status(self, id):
        booking = self.booking_service.get_by_id(id)
        if booking is None:
            return {"status":"error","message":"Service-booking not found"}
        is_active = self.booking_service.status(id)
        if is_active:
            return {"status":"success","message":"Service-booking Activated","data":is_active}
        return {"status":"success","message":"Service-booking Deactivated","data":is_active}

        # return redirect(url_for("booking.index"))

    def service_status(self,id,status_type,status):
        booking = self.booking_service.get_by_id(id)
        if booking is None:
             return {"status":"error","message": "Booking not found"}
        if status_type == 'payment':
            status_key = payment_statuses.get_key(status)
            updated_data = {
                'payment_status': status_key,
                'updated_at': datetime.now(),
                'updated_by': get_current_user().id
            }
        if status_type == 'booking':
            status_key = service_statuses.get_key(status)
            updated_data = {
                'service_status': status_key,
                'updated_at': datetime.now(),
                'updated_by': get_current_user().id
            }
        self.booking_service.update(id, **updated_data)
        return {"status":"success","message":f"{status_type} status chaged to {status}","data":status}

    def details(self,id):
        booking=self.booking_service.get_by_id(id)
        return render_template("admin/booking/details.html",booking=booking)


    


    ## customer controllers ##

    def bookings_page(self):
        return render_template("customer/my_bookings.html")