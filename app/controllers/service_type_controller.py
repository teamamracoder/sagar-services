from flask import render_template, redirect, url_for
from app.forms import CreateServiceTypeForm
from app.services import ServiceTypeService

service_type_service = ServiceTypeService()


class ServiceTypeController:

    def create(self):
        form = CreateServiceTypeForm()
        if form.validate_on_submit():
            service_type_service.create(
                created_by =  form.created_by.data,
                type_name =  form.type_name.data,
                service_img_url =  form.service_img_url.data
                )
            return redirect(url_for("service_type.index"))
        return render_template("admin/service_type/add.html", form=form)

    def get(self):
        service_types = service_type_service.get()
        return render_template("admin/service_type/index.html", service_types=service_types)

    def update(self, id):
        form = CreateServiceTypeForm()
        service_type = service_type_service.get_by_id(id)
        if not service_type:
            return redirect(url_for("service_type.index"))
        if form.validate_on_submit():
            service_type_service.update(id,
                            created_by = form.created_by.data,
                            type_name = form.type_name.data,
                            service_img_url = form.service_img_url.data
                            )
            return redirect(url_for("service_type.index"))
        form.created_by.data = service_type.created_by
        form.type_name.data = service_type.type_name
        form.service_img_url.data = service_type.service_img_url
        return render_template("admin/service_type/edit.html", form=form, id=id)
        
    def status(self, id):
        service_type_service.status(id)
        return redirect(url_for("service_type.index"))
        pass