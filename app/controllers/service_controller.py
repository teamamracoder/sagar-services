from flask import render_template, redirect, url_for
from app.forms import CreateServiceForm
from app.forms import UpdateServiceForm
from app.services import ServiceService


service_service = ServiceService()



class ServiceController:

    def create(self):
        form = CreateServiceForm()
        if form.validate_on_submit():
            service_service.create(
                created_by = form.created_by.data,
                service_name = form.service_name.data,
                description = form.description.data,
                service_charge = form.service_charge.data,
                available_area_pincode = form.available_area_pincode.data,
                payment_methods = form.payment_methods.data,
                discount = form.discount.data,
                service_img_urls = form.image.data.read(),
                # service_img_urls = form.service_img_urls.data,
                service_type_id = form.service_type_id.data
              )
            return redirect(url_for("service.index"))
        return render_template("admin/service/add.html", form=form)


    def get(self):
        services = service_service.get()
        return render_template("admin/service/index.html", services=services)

    def update(self, id):
        form = UpdateServiceForm()
        service = service_service.get_by_id(id)
        if not service:
            # Handle case where service doesn't exist
            return redirect(url_for("service.index"))
        if form.validate_on_submit():
            service_service.update(id,
                                created_by = form.created_by.data,
                                service_name = form.service_name.data,
                                description = form.description.data,
                                service_charge = form.service_charge.data,
                                available_area_pincode = form.available_area_pincode.data,
                                payment_methods = form.payment_methods.data,
                                discount = form.discount.data,
                                service_img_urls = form.service_img_urls.data,
                                service_type_id = form.service_type_id.data
                                )
            return redirect(url_for("service.index"))
        form.created_by.data = service.created_by
        form.service_name.data = service.service_name
        form.description.data = service.description
        form.service_charge.data = service.service_charge
        form.available_area_pincode.data = service.available_area_pincode
        form.payment_methods.data = service.payment_methods
        form.discount.data = service.discount
        form.service_img_urls.data = service.service_img_urls
        form.service_type_id.data = service.service_type_id
        return render_template("admin/service/edit.html", form=form, id=id)
    
    def status(self, id):
        service_service.status(id)
        return redirect(url_for("service.index"))
        pass