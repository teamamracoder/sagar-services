from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceForm, UpdateServiceForm
from app.services import ServiceService
from datetime import datetime



class ServiceController:
    def __init__(self) -> None:
        self.service_service = ServiceService()

    def create(self):
        form = CreateServiceForm()
        if form.validate_on_submit():
            self.service_service.create(
                created_by=form.created_by.data,
                created_at=datetime.now(),
                is_active=True,
                service_name=form.service_name.data,
                description=form.description.data,
                service_charge=form.service_charge.data,
                available_area_pincode=form.available_area_pincode.data,
                payment_methods=form.payment_methods.data,
                discount=form.discount.data,
                service_img_urls=form.service_img_urls.data,
                service_type_id=form.service_type_id.data
            )
            return redirect(url_for("service.index"))
        return render_template("admin/service/add.html", form=form)

    def get(self):
        return render_template("admin/service/index.html")

    def get_service_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "service_name", "description", "service_charge", "available_area_pincode", "payment_methods", "discount", "service_img_urls", "service_type_id"]
        data = self.service_service.get(request, columns)
        return jsonify(data)

    def update(self, id):
        service = self.service_service.get_by_id(id)
        form = UpdateServiceForm(obj=service)
        if form.validate_on_submit():
            self.service_service.update(
                id=id,
                created_by=service.created_by,
                created_at=service.created_at,
                updated_by=1,
                updated_at=datetime.now(),
                is_active=True,
                service_name=form.service_name.data,
                description=form.description.data,
                service_charge=form.service_charge.data,
                available_area_pincode=form.available_area_pincode.data,
                payment_methods=form.payment_methods.data,
                discount=form.discount.data,
                service_img_urls=form.service_img_urls.data,
                service_type_id=form.service_type_id.data
            )
            return redirect(url_for("service.index"))
        return render_template("admin/service/update.html", form=form, id=id)


    def status(self, id):
        service = self.service_service.get_by_id(id)
        if service is None:
            return render_template("admin/error/something_went_wrong.html")
        self.service_service.status(id)
        return redirect(url_for("service.index"))
