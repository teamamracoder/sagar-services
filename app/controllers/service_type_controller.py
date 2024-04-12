from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceTypeForm, UpdateServiceTypeForm
from app.services import ServiceTypeService
from datetime import datetime
from app.auth import get_current_user


class ServiceTypeController:
    def __init__(self) -> None:
        self.service_type_service = ServiceTypeService()

    def get(self):
        return render_template("admin/service_type/index.html")

    def get_service_type_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "type_name", "service_img_url"]
        data = self.service_type_service.get(request, columns)
        return jsonify(data)

    def create(self):
        form = CreateServiceTypeForm()
        if form.validate_on_submit():
            self.service_type_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                type_name =  form.type_name.data
            )
            return redirect(url_for("service_type.index"))
        return render_template("admin/service_type/add.html", form=form)

    def update(self, id):
        service_type = self.service_type_service.get_by_id(id)
        if service_type is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateServiceTypeForm(obj=service_type)

        if form.validate_on_submit():
            self.service_type_service.update(
                id=id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                type_name = form.type_name.data
            )
            return redirect(url_for("service_type.index"))
        return render_template("admin/service_type/update.html", form=form, id=id)
        
    def status(self, id):
        service_type = self.service_type_service.get_by_id(id)
        if service_type is None:
            return render_template("admin/error/something_went_wrong.html")
        self.service_type_service.status(id)
        if is_active:
            return {"status":"success","message":"Category Activated","data":is_active}
        return {"status":"success","message":"Category Deactivated","data":is_active}

       