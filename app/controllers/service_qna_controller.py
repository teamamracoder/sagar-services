from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceQnAForm, UpdateServiceQnAForm
from app.services import ServiceQuestionService, ServiceAnswerService, ServiceService, UserService
from datetime import datetime
from app.auth import get_current_user

class ServiceQnAController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.service_answer_service = ServiceAnswerService()
        self.service_question_service = ServiceQuestionService()
        self.user_service = UserService()

    def get(self):
        return render_template("admin/service_qna/index.html")

    def get_service_qna_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "service_id", "question", "user_id"]
        
        # Retrieve data related to service questions
        question_data = self.service_question_service.get(request, columns)
        
        # Add service names to the data
        data_with_services = self.service_service.add_service_with_this(question_data)
        
        # # Add answers to the data
        combined_data = self.service_answer_service.add_service_question_with_answer(question_data)
        
        # Return combined data as JSON response
        return jsonify(data_with_services)

    def create(self):
        form = CreateServiceQnAForm()
        if form.validate_on_submit():
            service = self.service_question_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                is_active=True,
                service_id = form.service_id.data,
                question = form.question.data,
                user_id =  form.user_id.data
            )
            self.service_answer_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                answer=form.answer.data,
                staff_id=get_current_user().id,
                question_id=question.id
            )
            return redirect(url_for("service_qna.index"))
        return render_template("admin/service_qna/add.html", form=form)

    def update(self, id):
        form = UpdateServiceQnAForm()
        question = self.service_question_service.get_by_id(id)
        answer=self.service_answer_service.get_answer_details_by_service_id(id)

        service = self.service_service.get_by_id(question.service_id)
        form.service_id.choices = [(service.id, service.service_name)]

        if form.validate_on_submit():
            service = self.service_question_service.update(
                id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                is_active=True,
                service_id=form.service_id.data,
                question=form.question.data,
                user_id=form.user_id.data
            )
            self.service_answer_service.update(
                answer.id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                answer=form.answer.data,
                staff_id=get_current_user().id,
                question_id=question.id
            )
            return redirect(url_for("service_qna.index"))
        return render_template("admin/service_qna/update.html",form=form,id=id,answer=answer,question=question)
        
    def status(self, id):
        service_question = self.service_question_service.get_by_id(id)
        if service_question is None:
            return render_template("admin/error/something_went_wrong.html")
        self.service_question_service.status(id)
        return redirect(url_for("service_qna.index"))

       