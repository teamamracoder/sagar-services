from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateStaffForm, UpdateStaffForm
from app.services import StaffService, UserService
from datetime import datetime
from app.auth import get_current_user

class StaffController:
    def __init__(self) -> None:
        self.staff_service = StaffService()
        self.user_service = UserService()

    def get(self):
        return render_template("admin/staff/index.html")

    def get_staff_data(self):
        columns = ["id", "user_id","name","email","salary","qualification","join_date","leave_date","department","is_active"]
        data = self.staff_service.get(request, columns)
        data = self.user_service.add_user_with_this(data)
        return jsonify(data)
    
    def create(self):
        form = CreateStaffForm()
        if form.validate_on_submit():
            self.stafff_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                staff_name=form.staff_name.data,
            )
            return redirect(url_for("staff.index"))
            # return render_template("admin/staf/add.html", form=form, error="staff already exists")
        return render_template("admin/staf/add.html", form=form)

    def update(self, id):
        staff = self.staff_service.get_by_id(id)
        if staff is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateStaffForm(obj=staff)
        
        if form.validate_on_submit():
            updated_data = {
                'staff_name': form.staff_name.data,
                'updated_at': datetime.now(),
                'updated_by': get_current_user().id
            }
            self.staff_service.update(id, **updated_data)
            return redirect(url_for("staff.index"))
        return render_template("admin/staf/update.html", id=id, form=form)

    def status(self, id):
        staff = self.staff_service.get_by_id(id)
        if staff is None:
            return render_template("admin/error/something_went_wrong.html")
        self.staff_service.status(id)
        return redirect(url_for("staff.index"))