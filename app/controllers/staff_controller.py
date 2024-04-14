from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateStaffForm, UpdateStaffForm
from app.services import StaffService, UserService, RoleService
from datetime import datetime
from app.auth import get_current_user
from app.constants import departments

class StaffController:
    def __init__(self) -> None:
        self.staff_service = StaffService()
        self.user_service = UserService()
        self.role_service= RoleService()

    def get(self):
        return render_template("admin/staff/index.html")

    def get_staff_data(self):
        columns = ["id", "user_id","name","email","salary","qualification","join_date","leave_date","department","is_active"]
        data = self.staff_service.get(request, columns)
        data = self.user_service.add_user_with_this(data)
        data = self.staff_service.add_departments_with_this(data)
        return jsonify(data)
    
    def create(self,user_id):
        logged_in_user,roles=get_current_user().values()
        form = CreateStaffForm()
        form.department.choices = departments.get_all_items()
        if form.validate_on_submit():
            self.staff_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                salary=form.salary.data,
                qualification=form.qualification.data,
                join_date=form.join_date.data,
                department=form.department.data,
                user_id=user_id
            )
            self.role_service.create(
                user_id=user_id, 
                role=2,
                created_by=logged_in_user.id,
                created_at=datetime.now()
            )
            return redirect(url_for("staff.index"))
        else:
            print(form.errors)
        
        return render_template("admin/staff/add.html", form=form, user_id=user_id)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        staff = self.staff_service.get_by_id(id)
        if staff is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateStaffForm(obj=staff)
        form.department.choices = departments.get_all_items()

        if form.validate_on_submit():
            updated_data = {
                'updated_at': datetime.now(),
                'updated_by': logged_in_user.id,
                'salary':form.salary.data,
                'qualification':form.qualification.data,
                'join_date':form.join_date.data,
                'leave_date':form.leave_date.data,
                'department':form.department.data
            }
            self.staff_service.update(id, **updated_data)
            return redirect(url_for("staff.index"))
        return render_template("admin/staff/update.html", id=id, form=form)

    def status(self, id):
        staff = self.staff_service.get_by_id(id)
        if staff is None:
            return {"status":"error","message":"Staff Not Found"}
        is_active=self.staff_service.status(id)
        role=self.role_service.get_role_by_user_id_and_role_key(staff.user_id,2)
        self.role_service.status(role.id)
        if is_active:
            return {"status":"success","message":"Staff Activated","data":is_active}
        return {"status":"success","message":"Staff Deactivated","data":is_active}
    
    def details(self,id):
        staff=self.staff_service.get_by_id(id)
        return render_template("admin/staff/details.html",staff=staff)