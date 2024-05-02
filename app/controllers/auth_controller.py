from datetime import datetime
import re
from flask import render_template, request, redirect, url_for, flash
import random

from app.forms import LoginForm
from app.forms.auth_forms import VerifyOtpForm
from app.forms.user_froms import CreateUserForm
from app.services import UserService
from app.auth import login, logout
from app.services.role_service import RoleService
from app.utils.file_utils import FileUtils
from app.utils.mail_utils import MailUtils
from app.utils.voice_utils import VOICEUtils
from app.utils import cache
from app.constants import email_templates

class AuthController:

    def __init__(self) -> None:
        self.user_service = UserService()
        self.role_service = RoleService()
    
    def send_mail(self,send_to:str, title:str, msg:str)->bool:
        is_sent = MailUtils.send(send_to,title,msg)
        if is_sent:
            return True
        return False

    def send_otp(self, user_id: int, type:str, send_to:str, msg:str) -> bool:
        otp = str(random.randint(100000, 999999))
        user = self.user_service.get_by_id(user_id)

        # send otp to mobile number or email
        if type=="mobile":
            send_status=VOICEUtils.voice_send(send_to, otp)
        else:
            msg = msg.replace("[OTP]",otp).replace("[FIRST_NAME]",user.first_name)
            send_status=self.send_mail(send_to,"otp verification",msg)
        if send_status:
            cache.set(user_id, otp, timeout=180)
            print(cache.get(user_id))
            return True
        else:
            return False

    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = self.user_service.get_user_by_email_or_mobile_and_password(
                form.email_or_mobile.data.strip(), form.password.data.strip()
            )
            if user:
                if user.is_active:
                    login(user)
                    next_page = request.args.get("next")
                    return redirect(next_page or url_for("home.index"))
                else:
                    return redirect(url_for('error_bp.deactivated'))
            else:
                flash("*Invalid username or password", "error")
        return render_template("auth/login.html", form=form)

    def signup(self):
        form = CreateUserForm()
        if form.validate_on_submit():
            email=form.email.data.strip()
            mobile=form.mobile.data.strip()

            prev_user = self.user_service.get_user_by_email(email)
            if prev_user:
                if not prev_user.is_verified:
                    msg = email_templates.get_value('OTP_TEMPLATE')
                    if self.send_otp(prev_user.id, "email", prev_user.email,msg):
                        flash("Account already exist with this email address, please verify to continue", "unverified")
                        return redirect(url_for("auth.verify_otp", id=prev_user.id))
                    else:
                        flash("Something went wrong!, please try again", "otp_error")
                        return render_template("auth/signup.html", form=form)

                flash("Email already exist", "email_error")
                return render_template("auth/signup.html", form=form)
            
            prev_user = self.user_service.get_user_by_mobile(mobile)
            if prev_user:
                if not prev_user.is_verified:
                    msg = ""
                    if self.send_otp(prev_user.id, "mobile", prev_user.mobile, msg):
                        flash("Account already exist with this Mobile no., please verify to continue", "unverified")
                        return redirect(url_for("auth.verify_otp", id=prev_user.id))
                    else:
                        flash("Something went wrong!, please try again", "otp_error")
                        return render_template("auth/signup.html", form=form)

                flash("Phone No. already exist", "mobile_error")
                return render_template("auth/signup.html", form=form)
            
            filepath = FileUtils.save("users", [form.profile_photo_url.data])
            user = self.user_service.create(
                email=email,
                password=form.password.data.strip(),
                first_name=form.first_name.data.strip(),
                last_name=form.last_name.data.strip(),
                mobile=mobile,
                created_at=datetime.now(),
                profile_photo_url=filepath,
                is_active=False,
                is_verified = False
            )
            self.role_service.create(
                user_id=user.id, role=3, created_by=user.id, created_at=datetime.now()
            )
            if user:
                login(user)
                msg = email_templates.get_value('OTP_TEMPLATE')
                if self.send_otp(user.id, "email", user.email,msg):
                    return redirect(url_for("auth.verify_otp", id=user.id))
                else:
                    flash("OTP sending failed, please try again", "otp_error")
        return render_template("auth/signup.html", form=form)

    def reset_password(self):
        return render_template("auth/reset_password.html")

    def verify_otp(self, user_id):
        form = VerifyOtpForm()
        ctp = cache.get(user_id)
        if form.validate_on_submit():
            otp_attempt = form.otp.data
            cached_otp = cache.get(user_id)

            if not cached_otp or cached_otp != otp_attempt:
                return {"error": "Invalid OTP"}

            # Clear OTP from cache after successful verification
            cache.delete(user_id)

            # update is_active column
            user = self.user_service.update(user_id, is_active=True, is_verified=True)
            if user:
                login(user)
                self.user_service.update(user.id, is_verified=True)
                msg = email_templates.get_value('WELCOME_TEMPLATE').replace("[FIRST_NAME]",user.first_name).replace("[FULL_NAME]",f"{user.first_name} {user.last_name}")
                self.send_mail(user.email,"verification succcessful",msg)
                return redirect(url_for("home.index"))
            else:
                flash("Invalid OTP", "otp_error")
        return render_template("auth/verify_otp.html", form=form, id=user_id)

    def logout(self):
        logout()
        return redirect(url_for("home.index"))

    def send_otp_for_reset_password(self):
        data = request.form.get("email_or_mob")

        if MailUtils.is_valid_email(data):
            # if email
            user = self.user_service.get_user_by_email(data)
            type = "email"
        elif data.isdigit():
            # if mobile
            user = self.user_service.get_user_by_mobile(data)
            type = "mobile"
        else:
            return {
                "status": "fail",
                "message": "Invalid email or mobile number.",
                "user_id": None,
            }

        if user:
            if type=="email":
                msg = email_templates.get_value('OTP_TEMPLATE')
                status=self.send_otp(user.id, type, user.email,msg)
            else:
                status=self.send_otp(user.id, type, user.mobile)

            if status:
                return {
                    "status": "success",
                    "message": "OTP send successfully.",
                    "user_id": user.id,
                }
            else:
                return {
                    "status": "fail",
                    "message": "OTP sending failed, please try again",
                    "user_id": user.id,
                }
        else:
            return {
                "status": "fail",
                "message": "User does not exist, please <a href='/signup'>signup</a>",
                "user_id": None,
            }

    def verify_otp_for_reset_password(self):
        otp = request.form.get("otp")
        user_id = request.form.get("user_id")

        cached_otp = cache.get(int(user_id))

        if not cached_otp or cached_otp != otp:
            return {"status": "fail", "message": "Invalid OTP.", "user_id": user_id}

        cache.delete(user_id)
        return {
            "status": "success",
            "message": "OTP verification successfull.",
            "user_id": user_id,
        }

    def change_password(self):
        new_password = request.form.get("new_password")
        user_id = request.form.get("user_id")
        user = self.user_service.update(user_id, password=new_password)
        if user:
            msg = email_templates.get_value('PASSWORD_CHANGE_TEMPLATE').replace("[FIRST_NAME]",user.first_name)
            self.send_mail(user.email,"password changed",msg)
            login(user)
            return {
                "status": "success",
                "message": "Password successfully changed.",
                "user_id": user_id,
            }
        else:
            return {
                "status": "fail",
                "message": "Password change failed.",
                "user_id": user_id,
            }
