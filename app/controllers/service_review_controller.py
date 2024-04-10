from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceReviewForm, UpdateServiceReviewForm
from app.services import ServiceReviewService, ServiceService
from datetime import datetime
from app.auth import get_current_user


class ServiceReviewController:
    def __init__(self) -> None:
        self.service_review_service = ServiceReviewService()
        self.service_service = ServiceService()

    def get(self):
        return render_template("admin/service_review/index.html")

    def get_service_review_data(self):
        # Determine the column to sort by
        columns = ["id","is_active","user_id","review_title","description","img_urls","rating","service_id","created_by","created_at","updated_by","updated_by"]
        data = self.service_review_service.get(request, columns)
        combined_data = self.service_service.add_service_with_this(data)
        return jsonify(combined_data)

    def create(self):
        form = CreateServiceReviewForm()
        services=self.service_service.get_active()
        form.service_id.choices = [(service.id, service.service_name) for service in services]
       
        if form.validate_on_submit():
            self.service_review_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                user_id=get_current_user().id,   
                review_title=form.review_title.data,
                description=form.description.data,
                # img_urls=form. img_urls.data,
                rating=form.rating.data,
                service_id=form.service_id.data,
            )
            return redirect(url_for("service_review.index"))
            # return render_template("admin/service_review/add.html", form=form, error="product_review already exists")
        return render_template("admin/service_review/add.html", form=form)

    def update(self, id):
        service_review = self.service_review_service.get_by_id(id)
        if service_review is None:
            return render_template("admin/error/something_went_wrong.html")
            

        service = self.service_service.get_by_id(service_review.service_id)
        print(service.id, service.service_name)
        form = UpdateServiceReviewForm(obj=service_review)
        form.service_id.choices = [(service.id, service.service_name)]

        if form.validate_on_submit():
            self.service_review_service.create(
                id=id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                user_id=get_current_user().id,   
                review_title=form.review_title.data,
                description=form.description.data,
                # img_urls=form. img_urls.data,
                rating=form.rating.data,
                service_id=form.service_id.data,
            )
            
            return redirect(url_for("service_review.index"))
        return render_template("admin/service_review/update.html", id=id, form=form)

    def status(self, id):
        service_review = self.service_review_service.get_by_id(id)
        if service_review is None:
            return render_template("admin/error/something_went_wrong.html")
        self.service_review_service.status(id)
        return redirect(url_for("service_review.index"))