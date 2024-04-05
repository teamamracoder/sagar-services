from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceAnswerForm,UpdateServiceAnswerForm
from app.services import ServiceAnswerService
from app.services import ServiceQuestionService
from datetime import datetime



class ServiceAnswerController:
    def __init__(self) -> None:
        self.service_answer_service = ServiceAnswerService()
        self.service_question_service = ServiceQuestionService()
        

    def create(self):
        form = CreateServiceAnswerForm()
        if form.validate_on_submit():
            self.service_answer_service.create(
                created_by =  form.created_by.data,
                created_at =  datetime.now(),
                is_active =  True,
                question_id =  form.question_id.data,
                answer =  form.answer.data,
                staff_id =  form.staff_id.data
                )
            return redirect(url_for("service_answer.index"))
        return render_template("admin/service_answer/add.html", form=form)

    def get(self):
        return render_template("admin/service_answer/index.html")

    def get_service_answer_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "question_id" "answer", "staff_id"]
        data = self.service_answer_service.get(request, columns)
        combined_data = self.service_question_service.add_answer_with_question(data)
        return jsonify(combined_data)

    def update(self, id):
        service_answer = self.service_answer_service.get_by_id(id)
        form = UpdateServiceAnswerForm(obj=service_answer)
        if form.validate_on_submit():
            self.service_answer_service.update(
                                id=id,
                                created_by = service_answer.created_by,
                                created_at = service_answer.created_at,
                                updated_by = 1,
                                updated_at = datetime.now(),
                                is_active=True,
                                question_id = form.question_id.data,
                                answer = form.answer.data,
                                staff_id = form.staff_id.data
                               )
            return redirect(url_for("service_answer.index"))
        return render_template("admin/service_answer/update.html", form=form, id=id)

    def status(self, id):
        service_answer = self.service_answer_service.get_by_id(id)
        if service_answer is None:
            return render_template("admin/error/something_went_wrong.html")
        self.service_answer_service.status(id)
        return redirect(url_for("service_answer.index"))

    