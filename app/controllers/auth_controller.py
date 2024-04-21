from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from flask_caching import Cache
import random

from app.forms import LoginForm
from app.forms.auth_forms import VerifyOtpForm
from app.forms.user_froms import CreateUserForm
from app.services import UserService
from app.auth import login, logout
from app.services.role_service import RoleService
from app.utils.file_utils import FileUtils

cache = {}


def init_cache(app):
    global cache
    cache = Cache(app, config={"CACHE_TYPE": "simple"})


class AuthController:

    def __init__(self) -> None:
        self.user_service = UserService()
        self.role_service = RoleService()
        self.cache = cache
        print(cache)

    def send_otp(self, user_id: int) -> None:
        otp = str(random.randint(100000, 999999))

        # send otp to mobile number or email

        self.cache.set(user_id, otp, timeout=180)

    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = self.user_service.get_user_by_email_and_password(
                form.email.data, form.password.data
            )
            if user:
                login(user)
                next_page = request.args.get("next")
                return redirect(next_page or url_for("home.index"))
            else:
                flash("Invalid username or password", "error")
        return render_template("auth/login.html", form=form)

    def signup(self):
        form = CreateUserForm()
        if form.validate_on_submit():
            filepath = FileUtils.save("users", [form.profile_photo_url.data])
            user = self.user_service.create(
                email=form.email.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                mobile=form.mobile.data,
                created_at=datetime.now(),
                profile_photo_url=filepath,
                is_active=False,
            )
            self.role_service.create(
                user_id=user.id, role=3, created_by=user.id, created_at=datetime.now()
            )

            if user:
                self.send_otp(user.id)
                return redirect(url_for("auth.verify_otp", id=user.id))
        return render_template("auth/signup.html", form=form)

    def reset_password(self):
        return render_template("auth/reset_password.html")

    def verify_otp(self, user_id):
        form = VerifyOtpForm()
        ctp = self.cache.get(user_id)
        print(ctp)
        if form.validate_on_submit():
            otp_attempt = form.otp.data
            cached_otp = self.cache.get(user_id)

            if not cached_otp or cached_otp != otp_attempt:
                return {"error": "Invalid OTP"}

            # Clear OTP from cache after successful verification
            self.cache.delete(user_id)

            # update is_active column
            user = self.user_service.update(user_id, is_active=True)

            if user:
                login(user)
                return redirect(url_for("home.index"))
            else:
                flash("Invalid OTP", "error")
        return render_template("auth/verify_otp.html", form=form)

    def logout(self):
        logout()
        return redirect(url_for("home.index"))
