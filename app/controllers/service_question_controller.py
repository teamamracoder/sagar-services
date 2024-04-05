from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceQuestionForm, UpdateServiceQuestionForm
from app.services import ServiceQuestionService
from app.services import UserService
from datetime import datetime


class ServiceQuestionController:
    def __init__(self) -> None:
        self.service_question_service = ServiceQuestionService()
        self.user_service = UserService()

    def create(self):
        form = CreateServiceQuestionForm()
        if form.validate_on_submit():
            self.service_question_service.create(
                created_by=form.created_by.data,
                created_at=datetime.now(),
                is_active=True,
                service_id = form.service_id.data,
                question = form.question.data,
                user_id =  form.user_id.data
            )
            return redirect(url_for("service_question.index"))
        return render_template("admin/service_question/add.html", form=form)

    def get(self):
        return render_template("admin/service_question/index.html")

    def get_service_question_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "service_id", "question", "user_id"]
        data = self.service_question_service.get(request, columns)
        return jsonify(data)

    def update(self, id):
        service_question = self.service_question_service.get_by_id(id)
        form = UpdateServiceQuestionForm(obj=service_question)
        if form.validate_on_submit():
            self.service_question_service.update(
                id=id,
                created_by = service_question.created_by,
                created_at = service_question.created_at,
                updated_by = 1,
                updated_at = datetime.now(),
                is_active = True,
                question = form.question.data,
                user_id = form.user_id.data
            )
            return redirect(url_for("service_question.index"))
        return render_template("admin/service_question/update.html",form=form, id=id)
        
    def status(self, id):
        service_question = self.service_question_service.get_by_id(id)
        if service_question is None:
            return render_template("admin/error/something_went_wrong.html")
        self.service_question_service.status(id)
        return redirect(url_for("service_question.index"))

       