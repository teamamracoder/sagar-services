from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateRoleForm
from app.services import RoleService


class RoleController:

    def __init__(self) -> None:
        self.role_service = RoleService()

    def create(self):
        form = CreateRoleForm()
        if form.validate_on_submit():
            self.role_service.create(user_id=form.user_id.data, role=form.role.data)
            return redirect(url_for("role.index"))
        return render_template("admin/role/add.html", form=form)

    def get(self):
        return render_template("admin/role/index.html")

    def get_role_data(self):
        # Determine the column to sort by
        columns = ["id", "role", "user_id"]
        data = self.role_service.get(request, columns)
        return jsonify(data)
