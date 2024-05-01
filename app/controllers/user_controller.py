from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateUserForm, UpdateUserForm
from app.services import UserService, RoleService
from app.constants import roles
from datetime import datetime
from app.auth import get_current_user
from app.utils import FileUtils

class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()
        self.role_service = RoleService()

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateUserForm()
        if form.validate_on_submit():
            filepath=FileUtils.save('users',[form.profile_photo_url.data])
            self.user_service.create(
                email=form.email.data.strip(),
                password=form.password.data.strip(),
                first_name=form.first_name.data.strip(),
                last_name=form.last_name.data.strip(),
                mobile=form.mobile.data.strip(),
                landmark=form.landmark.data,
                address_line=form.address_line.data,
                city=form.city.data,
                state=form.state.data,
                street=form.street.data,
                pincode=form.pincode.data,
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                dob=form.dob.data,
                gender=form.gender.data,
                profile_photo_url=filepath
            )
            return redirect(url_for("user.index"))
        return render_template("admin/user/add.html", form=form)

    def get(self):
        logged_in_user,roles=get_current_user().values()
        return render_template("admin/user/index.html",user_id=logged_in_user.id)

    def get_user_data(self):
        columns = ["id", "first_name", "email", "is_active", "mobile", "last_name", "profile_photo_url"]
        data = self.user_service.get(request, columns)
        data = self.role_service.add_roles_with_users(data)
        return jsonify(data)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        user = self.user_service.get_by_id(id)
        form = UpdateUserForm(obj=user)
        if form.validate_on_submit():
            filepath=user.profile_photo_url
            new_filepath=FileUtils.save('users',[form.profile_photo_url.data])
            if new_filepath:
                FileUtils.delete(filepath)
                filepath=new_filepath
            self.user_service.update(
                id=id,
                email=form.email.data.strip(),
                first_name=form.first_name.data.strip(),
                last_name=form.last_name.data.strip(),
                mobile=form.mobile.data.strip(),
                dob=form.dob.data,
                gender=form.gender.data,
                landmark=form.landmark.data,
                address_line=form.address_line.data,
                city=form.city.data,
                state=form.state.data,
                street=form.street.data,
                pincode=form.pincode.data,
                profile_photo_url=filepath,
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
    
    def admin_my_profile(self):
        logged_in_user,roles=get_current_user().values()
        user = self.user_service.get_by_id(logged_in_user.id)
        form = UpdateUserForm(obj=user)
        return render_template("admin/user/my_profile.html",form=form, user=user)

    def admin_my_profile_update(self):
        logged_in_user,roles=get_current_user().values()
        user = self.user_service.get_by_id(logged_in_user.id)
        form = UpdateUserForm(obj=user)
        filepath=user.profile_photo_url
        new_filepath=FileUtils.save('users',[form.profile_photo_url.data])
        if new_filepath:
            FileUtils.delete(filepath)
            filepath=new_filepath
        self.user_service.update(
            id=logged_in_user.id,
            email=form.email.data.strip(),
            first_name=form.first_name.data.strip(),
            last_name=form.last_name.data.strip(),
            mobile=form.mobile.data.strip(),
            updated_by=logged_in_user.id,
            gender = form.gender.data,
            dob = form.dob.data,
            landmark=form.landmark.data,
            address_line=form.address_line.data,
            city=form.city.data,
            state=form.state.data,
            street=form.street.data,
            pincode=form.pincode.data,
            updated_at=datetime.now(),
            profile_photo_url=filepath
        )
        return render_template("admin/user/my_profile.html",user=user,form=form)





    ## customer controllers ##


    def my_profile_page(self):
        logged_in_user,roles=get_current_user().values()
        user = self.user_service.get_by_id(logged_in_user.id)
        form = UpdateUserForm(obj=user)
        return render_template("customer/my_profile.html",form=form, user=user)
    
    def my_profile_update(self):
        logged_in_user,roles=get_current_user().values()
        user = self.user_service.get_by_id(logged_in_user.id)
        form = UpdateUserForm(obj=user)
        filepath=user.profile_photo_url
        new_filepath=FileUtils.save('users',[form.profile_photo_url.data])
        if new_filepath:
            FileUtils.delete(filepath)
            filepath=new_filepath
        self.user_service.update(
            id=logged_in_user.id,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            mobile=form.mobile.data,
            updated_by=logged_in_user.id,
            gender = form.gender.data,
            dob = form.dob.data,
            landmark=form.landmark.data,
            address_line=form.address_line.data,
            city=form.city.data,
            state=form.state.data,
            street=form.street.data,
            pincode=form.pincode.data,
            updated_at=datetime.now(),
            profile_photo_url=filepath
        )
        return render_template("customer/my_profile.html",user=user,form=form)