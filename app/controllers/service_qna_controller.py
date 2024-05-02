from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceQnAForm, UpdateServiceQnAForm
from app.services import ServiceQnAService, ServiceService, UserService, BookingService
from datetime import datetime
from app.auth import get_current_user

class ServiceQnAController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.service_qna_service = ServiceQnAService()
        self.user_service = UserService()
        self.booking_service = BookingService()

    def get(self):
        return render_template("admin/service_qna/index.html")

    def get_service_qna_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "service_id", "question", "answer" "user_id"]
        question_data = self.service_qna_service.get(request, columns)
        combined_data = self.service_service.add_service_with_this(question_data)
        return jsonify(combined_data)

    # def create(self):
    #     logged_in_user,roles=get_current_user().values()
    #     form = CreateServiceQnAForm()
    #     services=self.service_service.get_active()
    #     form.service_id.choices = [(service.id, service.service_name) for service in services]
       
    #     if form.validate_on_submit():
    #         service = self.service_qna_service.create(
    #             created_by=logged_in_user.id,
    #             created_at=datetime.now(),
    #             service_id = form.service_id.data,
    #             question = form.question.data,
    #             user_id = logged_in_user.id
    #         )
    #         return redirect(url_for("service_qna.index"))
    #     return render_template("admin/service_qna/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        qna = self.service_qna_service.get_by_id(id)
        if qna is None:
            return render_template("admin/error/something_went_wrong.html")

        service=self.service_service.get_by_id(qna.service_id)
        form = UpdateServiceQnAForm(obj=qna)
        form.service_id.choices = [(service.id, service.service_name)]
        if form.validate_on_submit():
            self.service_qna_service.update(
                id=id,
                updated_by=logged_in_user.id,
                updated_at=datetime.now(),
                service_id=form.service_id.data,
                question=form.question.data,
                answer=form.answer.data,
                user_id=logged_in_user.id
            )
            return redirect(url_for("service_qna.index"))
        return render_template("admin/service_qna/update.html",form=form,id=id)
        
    def status(self, id):
        service_qna = self.service_qna_service.get_by_id(id)
        if service_qna is None:
            return {"status":"error","message":"Service-type not found"}
        is_active = self.service_qna_service.status(id)
        if is_active:
            return {"status":"success","message":"Service QnA's Activated","data":is_active}
        return {"status":"success","message":"Service QnA's Deactivated","data":is_active}

        # return redirect(url_for("service_qna.index"))

       


    # cutomer 
    def service_qna_create(self,service_id):
        logged_in_user,roles=get_current_user().values()
        qnaForm = CreateServiceQnAForm()
        services = self.service_service.get_by_id(service_id)

        if qnaForm.validate_on_submit():
            is_booked = self.booking_service.get_by_user_and_service_id(service_id, logged_in_user.id)
            is_qna = self.service_qna_service.get_check_is_qna_or_not(service_id, logged_in_user.id)
            if is_booked:
                if is_qna is None:
                    service = self.service_qna_service.create(
                        created_by=logged_in_user.id,
                        created_at=datetime.now(),
                        service_id = qnaForm.service_id.data,
                        question = qnaForm.question.data,
                        user_id = logged_in_user.id
                    )
                    service=self.service_service.get_by_id(service_id)
                    return redirect(url_for("service.service_details_page",service_id=service_id))

                error_message = "Can't ask any query..! Already done..."
                return redirect(url_for("service.service_details_page", service_id=service_id, error=error_message))
 
            error_message = "Can't give ask any question..! Book the service first."
            return redirect(url_for("service.service_details_page", service_id=service_id, error=error_message))

        return redirect(url_for("service.service_details_page",service_id=service_id,qnaForm=qnaForm))
