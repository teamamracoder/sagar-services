from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateContactForm, UpdateContactForm
from app.services import ContactService, RoleService
from app.utils import FileUtils


class ContactController:
    def __init__(self) -> None:
        self.contact_service = ContactService()
        self.role_service = RoleService()

    def create(self):
        form = CreateContactForm()
        if form.validate_on_submit():
            filepath=FileUtils.save('contacts',form.query_img_urls.data)
            if isinstance(filepath,str):
                filepath=[filepath]

            self.contact_service.create(
                email=form.email.data,
                name=form.name.data,
                phone=form.phone.data,
                query_message=form.query_message.data,
                query_img_urls=filepath
            )
            return redirect(url_for("contact_bp.index"))
        return render_template("admin/contact/add.html", form=form)

    def get(self):
        return render_template("admin/contact/index.html")

    def get_contact_data(self):
        # Determine the column to sort by
        columns = ["id", "name", "email","phone","query_message","is_active"]
        data = self.contact_service.get(request, columns)
        # contact_data = self.role_service.add_roles_with_users(data)
        return jsonify(data)

    def update(self,id):
        user = self.contact_service.get_by_id(id)
        form = UpdateContactForm(obj=user)
        if form.validate_on_submit():
            self.contact_service.update(
                id=id,
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                query_message=form.query_message.data,
                query_img_urls=form.query_img_urls.data
            )
            return redirect(url_for("contact_bp.index"))
        return render_template("admin/contact/update.html", id=id,form=form)

    def status(self,id):
        contact = self.contact_service.get_by_id(id)
        if contact is None:
            return render_template("admin/error/something_went_wrong.html")
        self.contact_service.status(id)
        return redirect(url_for("contact_bp.index"))



    ## customer controller ##

    def contact_us_page(self):
        form = CreateContactForm()
        if form.validate_on_submit():
            filepath=FileUtils.save('contacts',form.query_img_urls.data)
            if isinstance(filepath,str):
                filepath=[filepath]
            self.contact_service.create(
                email=form.email.data,
                name=form.name.data,
                phone=form.phone.data,
                query_message=form.query_message.data,
                query_img_urls=filepath
            )
            return redirect(url_for("home.index"))
        return render_template("customer/contact_us.html", form=form)