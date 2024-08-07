from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceReviewForm
from app.services import ServiceReviewService, ServiceService, BookingLogService, BookingService
from datetime import datetime
from app.auth import get_current_user
from app.utils import FileUtils


class ServiceReviewController:
    def __init__(self) -> None:
        self.service_review_service = ServiceReviewService()
        self.service_service = ServiceService()
        self.booking_log_service = BookingLogService()
        self.booking_service = BookingService()

    def get(self):
        return render_template("admin/service_review/index.html")

    def get_service_review_data(self):
        # Determine the column to sort by
        columns = ["id","is_active","user_id","review_title","description","img_urls","rating","service_id","created_by","created_at","updated_by","updated_by"]
        data = self.service_review_service.get(request, columns)
        combined_data = self.service_service.add_service_with_this(data)
        return jsonify(combined_data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateServiceReviewForm()
        services=self.service_service.get_active()
        form.service_id.choices = [(service.id, service.service_name) for service in services]
       
        if form.validate_on_submit():
            filepath=FileUtils.save('service_reviews',form.service_review_img_urls.data)
            if isinstance(filepath,str):
                filepath=[filepath]
            self.service_review_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                user_id=logged_in_user.id,   
                review_title=form.review_title.data,
                description=form.description.data,
                service_review_img_urls=filepath,
                rating=form.rating.data,
                service_id=form.service_id.data,
            )
            return redirect(url_for("service_review.index"))
            # return render_template("admin/service_review/add.html", form=form, error="product_review already exists")
        return render_template("admin/service_review/add.html", form=form)

    # def update(self, id):
    #     logged_in_user,roles=get_current_user().values()
    #     service_review = self.service_review_service.get_by_id(id)
    #     if service_review is None:
    #         return render_template("admin/error/something_went_wrong.html")
            

    #     service = self.service_service.get_by_id(service_review.service_id)
    #     print(service.id, service.service_name)
    #     form = UpdateServiceReviewForm(obj=service_review)
    #     form.service_id.choices = [(service.id, service.service_name)]

    #     if form.validate_on_submit():
    #         filepath=FileUtils.save('service_reviews',*form.service_review_img_urls.data)
    #         self.service_review_service.create(
    #             id=id,
    #             updated_by=logged_in_user.id,
    #             updated_at=datetime.now(),
    #             user_id=logged_in_user.id,   
    #             review_title=form.review_title.data,
    #             description=form.description.data,
    #             service_review_img_urls=filepath,
    #             rating=form.rating.data,
    #             service_id=form.service_id.data,
    #         )
            
    #         return redirect(url_for("service_review.index"))
    #     return render_template("admin/service_review/update.html", id=id, form=form)

    def status(self, id):
        service_review = self.service_review_service.get_by_id(id)
        if service_review is None:
            return {"status":"error","message":"Service-review not found","data":is_active}
        is_active = self.service_review_service.status(id)
        if is_active:
            return {"status":"success","message":"Service-review Activated","data":is_active}
        return {"status":"success","message":"Service-review Deactivated","data":is_active}

        # return redirect(url_for("service_review.index"))



    def service_review_create(self, service_id):
        logged_in_user, roles = get_current_user().values()
        reviewForm = CreateServiceReviewForm()

        if reviewForm.validate_on_submit():
            is_booked = self.booking_service.get_by_user_and_service_id(service_id, logged_in_user.id)
            is_review = self.service_review_service.get_check_is_review_or_not(service_id, logged_in_user.id)
            
            if is_booked:
                if is_review is None:
                    # Proceed with creating the review
                    filepath = FileUtils.save('service_reviews', reviewForm.service_review_img_urls.data)
                    if isinstance(filepath, str):
                        filepath = [filepath]

                    self.service_review_service.create(
                        created_by=logged_in_user.id,
                        created_at=datetime.now(),
                        user_id=logged_in_user.id,   
                        review_title=reviewForm.review_title.data,
                        description=reviewForm.description.data,
                        service_review_img_urls=filepath,
                        rating=reviewForm.rating.data,
                        service_id=reviewForm.service_id.data,
                    )
                    return redirect(url_for("service.service_details_page", service_id=service_id))

               # If the user has already given feedback, redirect with an error message
                error_message = "Can't give any feedback! Already done..."
                return redirect(url_for("service.service_details_page", service_id=service_id, error=error_message))
 
            # If the service is not booked by the user, redirect with an error message
            error_message = "Can't give any feedback! Book the service first."
            return redirect(url_for("service.service_details_page", service_id=service_id, error=error_message))

        # If form validation fails, redirect back to the service details page with the form data
        return redirect(url_for("service.service_details_page", service_id=service_id, reviewForm=reviewForm))
