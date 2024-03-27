from flask import render_template, redirect, url_for
from app.forms import CreateUserForm
from app.services import UserService

user_service = UserService()


class UserController:

    def create(self):
        form = CreateUserForm()
        if form.validate_on_submit():
            user_service.create(
                email=form.email.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                mobile=form.mobile.data,
            )
            return redirect(url_for("user_bp.index"))
        return render_template("admin/user/add.html", form=form)

    def get(self):
        users = user_service.get()
        roles = {1: "ADMIN", 2: "STAFF", 3: "CUSTOMER"}
        return render_template("admin/user/index.html", users=users, roles=roles)
