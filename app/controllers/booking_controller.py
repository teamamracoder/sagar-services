from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateBookingForm,UpdateBookingForm
from app.services import ServiceService,BookingService,BookingLogService,UserService,StaffService
from datetime import datetime
from app.constants import payment_methods
from app.constants import service_statuses
from app.constants import payment_statuses
from app.auth import get_current_user
from app.constants import email_templates
from app.utils.mail_utils import MailUtils
from app.utils import cache

class BookingController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.booking_service = BookingService()
        self.user_service = UserService()
        self.staff_service = StaffService()
        self.booking_log_service = BookingLogService()

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
            booking = self.booking_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                service_id=form.service_id.data,
                user_id=logged_in_user.id,
                total_charges=form.total_charges.data,
                service_location=form.service_location.data,
                service_status=form.service_status.data,
                payment_status=form.payment_status.data,
                payment_method=form.payment_method.data,
                area_pincode=form.area_pincode.data,
            )
            booked_service=self.booking_service.get_by_id(booking.service_id) # insert status in booking_log
            self.booking_log_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                booking_id=booking.id,
                booking_status=booking.service_status
            )
            return redirect(url_for("booking.index"))
        return render_template("admin/booking/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        booking = self.booking_service.get_by_id(id)
        if booking is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateBookingForm(obj=booking)

        
        staffs = self.staff_service.get_active()
        staffs_id = [(staff.id, staff.id) for staff in staffs]
        staff_details = []
        for staff_id, _ in staffs_id:
            staff_detail = self.user_service.get_by_id(staff_id)
            staff_details.append(staff_detail)
        form.staff_id.choices = [(staff.id, staff.first_name) for staff in staff_details]
        
        
        # get_staffs_from_user = self.user_service.get_by_id(staffs_id)

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
                area_pincode=form.area_pincode.data,
                booking_details=form.booking_details.data
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
        logged_in_user,roles=get_current_user().values()
        booking = self.booking_service.get_by_id(id)
        if booking is None:
             return {"status":"error","message": "Booking not found"}
        else:
            if status_type == 'payment':
                status_key = payment_statuses.get_key(status)
                updated_data = {
                    'payment_status': status_key,
                    'updated_at': datetime.now(),
                    'updated_by': 1
                }
                self.booking_service.update(id, **updated_data)
                return {"status":"success","message":f"{status_type} status chaged to {status}","data":status}

            if status_type == 'booking':
                service_new_status = service_statuses.get_key(status)
                # get previous booking status
                service_prev_status=booking.service_status
                service_prev_status_name = service_statuses.get_value(service_prev_status)
                if service_prev_status!=3 and service_prev_status!=4:
                    if service_new_status>=service_prev_status :
                        # update booking table
                        updated_data = {
                            'service_status': service_new_status,
                            'updated_at': datetime.now(),
                            'updated_by': 1
                        }
                        self.booking_service.update(id, **updated_data)
                        # insert status in booking_log
                        self.booking_log_service.create(
                            created_by=logged_in_user.id,
                            created_at=datetime.now(),
                            booking_id=booking.id,
                            booking_status=service_new_status
                        )
                        self.booking_service.update(id, payment_status=1)
                        return {"status":"success","message":f"{status_type} status chaged to {status}","data":status, "key":service_new_status}
                    else:
                        return {"status":"error","message":f"{status_type} status can not be changed to old step","data":status}
                else:
                    return {"status":"error","message":f"{status_type} is already {service_prev_status_name} so, can not change status","data":status}
            else:
                return {"status":"error","message":f"{status_type} status can not be chaged","data":status}



    def details(self,id):
        booking = self.booking_service.get_by_id(id)
        service = self.service_service.get_by_id(booking.service_id)
        user = self.user_service.get_by_id(booking.user_id)
        payment_status = payment_statuses.get_value(booking.payment_status)
        staff = self.staff_service.get_by_id(booking.staff_id)
        booking_logs = self.booking_log_service.get_booking_log_by_booking_id(id)
        if booking.staff_id:
            get_user_id = self.staff_service.get_by_user_id(booking.staff_id) 
            staffs = self.user_service.get_by_id(get_user_id.user_id)
        else:
            staffs = []
        return render_template("admin/booking/details.html",booking=booking,service=service,user=user,payment_status=payment_status,booking_logs=booking_logs,staffs=staffs)





    ## customer controllers ##

    def bookings_page(self):
        return render_template("customer/my_bookings.html")

    def bookings_page_data(self):
        logged_in_user,roles=get_current_user().values()
        columns = ["id", "created_at", "service_id","staff_id","total_charges","service_location","service_status","area_pincode", "payment_status","payment_method"]
        data = self.booking_service.get_bookings_by_user_id(logged_in_user.id,request, columns)
        data = self.service_service.add_service_with_this(data)
        data = self.booking_log_service.add_booking_latest_log(data)
        data = self.booking_service.add_payment_status_name_with_this(data)
        data = self.booking_service.add_payment_method_with_this(data)
        return jsonify(data)


    def booking_create(self,service_id):
        logged_in_user,roles=get_current_user().values()
        service = self.service_service.get_by_id(service_id)
        if service:
            return render_template('customer/book_now.html',service=service, user=logged_in_user)
        return render_template('customer/index.html')

    def confirm(self):
        logged_in_user,roles=get_current_user().values()
        service_id = int(request.form.get('service_id'))
        service = self.service_service.get_by_id(service_id)
        is_new_address = request.form.get('new-address')
        
        if is_new_address:
            service_location = request.form.get("StreetAddress")+","+request.form.get("Landmark")+","+request.form.get("Additional Address")+","+request.form.get("City")+","+request.form.get("State")
            area_pincode=request.form.get("PinCode")
            mobile = request.form.get("MobileNo")
        else:
            mobile = logged_in_user.mobile
            service_location = ",".join(
                str(attr) for attr in [
                    logged_in_user.landmark,
                    logged_in_user.address_line,
                    logged_in_user.city,
                    logged_in_user.state,
                    logged_in_user.street
                ] if attr is not None or attr != ''
            )
            area_pincode = logged_in_user.pincode
        if request.form.get("pay_method")=='1':
            payment_status = 2
        else:
            payment_status = 1
            
        booking_details={
            "created_by":logged_in_user.id,
            "created_at":datetime.now(),
            "user_id":logged_in_user.id,
            "payment_method":request.form.get("pay_method"),
            "area_pincode":area_pincode,
            "service_location":service_location,
            "mobile":mobile,
            "payment_status":payment_status,
            "service_id":service_id,
            "total_charges":service.service_charge-service.discount,
            "service_status":1
        }
        
        booking = self.booking_service.create(**booking_details)
        self.booking_log_service.create(
            created_by=logged_in_user.id,
            created_at=datetime.now(),
            booking_id=booking.id,
            booking_status=booking.service_status
        )
        
        if is_new_address:
            if not logged_in_user.pincode:
                self.user_service.update(
                    logged_in_user.id,
                    landmark = request.form.get("Landmark"),
                    address_line = request.form.get("Additional Address"),
                    city = request.form.get("City"),
                    state = request.form.get("State"),
                    street = request.form.get("StreetAddress"),
                    pincode = int(request.form.get("PinCode").strip())
                )

        msg = email_templates.get_value('BOOKING_THANK_YOU_TEMPLATE').replace("[FULL_NAME]",f"{logged_in_user.first_name} {logged_in_user.last_name}")
        MailUtils.send(logged_in_user.email, "Booking Confirmed", msg)
        cache.set("booking_success_"+ str(logged_in_user.id), True)
        return redirect(url_for("booking.booking_success"))
    
    def booking_success(self):
        logged_in_user,roles=get_current_user().values()
        success_check = cache.get("booking_success_"+ str(logged_in_user.id))
        if success_check:
            msg = email_templates.get_value('BOOKING_THANK_YOU_TEMPLATE').replace("[FULL_NAME]",f"{logged_in_user.first_name} {logged_in_user.last_name}")
            MailUtils.send(logged_in_user.email, "Booking Confirmed", msg)
            cache.delete("booking_success_"+ str(logged_in_user.id))
            return render_template("customer/booking_success.html")
        else:
            return redirect(url_for("home.index"))


    def booking_details_page(self,booking_id):
        booking=self.booking_service.get_by_id(booking_id)
        service = self.service_service.get_by_id(booking.service_id)
        user = self.user_service.get_by_id(booking.user_id)
        payment_method = payment_methods.get_value(booking.payment_method)
        payment_status = payment_statuses.get_value(booking.payment_status)
        booking_logs= self.booking_log_service.get_booking_log_by_booking_id(booking_id)
        return render_template("customer/booking_details.html",booking=booking,booking_logs=booking_logs,service=service,user=user,payment_status=payment_status,payment_method=payment_method)
    

    def cancel(self,booking_id):
        logged_in_user,roles=get_current_user().values()
        booking = self.booking_service.get_by_id(booking_id)
        booking_prev_status=booking.service_status
        if booking_prev_status == 1:
            updated_data = {
                'service_status': 4,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
            self.booking_service.update(id, **updated_data)
            self.booking_log_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                booking_id=booking.id,
                booking_status=4
            )
        return redirect(url_for("booking.bookings_page"))

