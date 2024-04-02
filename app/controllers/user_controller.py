from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateUserForm, UpdateUserForm
from app.services import UserService, RoleService


class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()
        self.role_service = RoleService()

    def create(self):
        form = CreateUserForm()
        if form.validate_on_submit():
            self.user_service.create(
                email=form.email.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                mobile=form.mobile.data,
            )
            return redirect(url_for("user.index"))
        return render_template("admin/user/add.html", form=form)

    def get(self):
        return render_template("admin/user/index.html")

    def get_user_data(self):
        # Determine the column to sort by
        columns = ["id", "first_name", "email","is_active"]
        data = self.user_service.get(request, columns)
        user_data = self.role_service.add_roles_with_users(data)
        return jsonify(user_data)

    def update(self,id):
        user = self.user_service.get_by_id(id)
        form = UpdateUserForm(obj=user)
        if form.validate_on_submit():
            self.user_service.update(
                id=id,
                email=form.email.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                mobile=form.mobile.data,
            )
            return redirect(url_for("user.index"))
        return render_template("admin/user/update.html", id=id,form=form)

    def status(self,id):
        user = self.user_service.get_by_id(id)
        if user is None:
            return render_template("admin/error/something_went_wrong.html")
        self.user_service.status(id)
        return redirect(url_for("user.index"))