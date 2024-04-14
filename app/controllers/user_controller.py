from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateUserForm, UpdateUserForm
from app.services import UserService, RoleService
from app.constants import roles
from datetime import datetime
from app.auth import get_current_user


class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()
        self.role_service = RoleService()

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateUserForm()
        if form.validate_on_submit():
            self.user_service.create(
                email=form.email.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                mobile=form.mobile.data,
                created_by=logged_in_user.id,
                created_at=datetime.now()
            )
            return redirect(url_for("user.index"))
        return render_template("admin/user/add.html", form=form)

    def get(self):
        return render_template("admin/user/index.html")

    def get_user_data(self):
        columns = ["id", "first_name", "email", "is_active", "mobile", "last_name"]
        data = self.user_service.get(request, columns)
        data = self.role_service.add_roles_with_users(data)
        return jsonify(data)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
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
                updated_by=logged_in_user.id,
                updated_at=datetime.now()
            )
            return redirect(url_for("user.index"))
        return render_template("admin/user/update.html", id=id, form=form)

    def status(self, id):
        user = self.user_service.get_by_id(id)
        if user is None:
            return {"status":"error","message":"User Not Found"}
        is_active=self.user_service.status(id)
        if is_active:
            return {"status":"success","message":"User Activated","data":is_active}
        return {"status":"success","message":"User Deactivated","data":is_active}

    def details(self,id):
        user=self.user_service.get_by_id(id)
        return render_template("admin/user/details.html",user=user)