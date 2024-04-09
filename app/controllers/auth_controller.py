from flask import render_template, request, redirect, url_for, flash

from app.forms import LoginForm
from app.services import UserService
from app.auth import login, logout

user_service = UserService()


class AuthController:

    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = user_service.get_user_by_email_and_password(
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
        return render_template("auth/signup.html")

    def reset_password(self):
        return render_template("auth/reset_password.html")

    def logout(self):
        logout()
        return redirect(url_for("home.index"))
