from flask import render_template, redirect, url_for
from app.forms import CreateRoleForm
from app.services import RoleService

role_service = RoleService()


class RoleController:

    def create(self):
        form = CreateRoleForm()
        if form.validate_on_submit():
            role_service.create(form.user_id.data, form.role.data)
            return redirect(url_for("role_bp.index"))
        return render_template("admin/role/add.html", form=form)

    def get(self):
        roles = role_service.get()
        return render_template("admin/role/index.html", roles=roles)
