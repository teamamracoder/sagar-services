from flask import render_template, redirect, url_for
from app.forms import CreateServiceQuestionForm
from app.services import ServiceQuestionService

service_question_service = ServiceQuestionService()


class ServiceQuestionController:

    def create(self):
        form = CreateServiceQuestionForm()
        if form.validate_on_submit():
            service_question_service.create(
                created_by =  form.created_by.data,
                service_id =  form.service_id.data,
                question =  form.question.data,
                user_id =  form.user_id.data
                )
            return redirect(url_for("service_question.index"))
        return render_template("admin/service_question/add.html", form=form)

    def get(self):
        service_questions = service_question_service.get()
        return render_template("admin/service_question/index.html", service_questions=service_questions)

    def update(self, id):
        form = CreateServiceQuestionForm()
        service_question = service_question_service.get_by_id(id)
        if not service_question:
            # Handle case where service_question doesn't exist
            return redirect(url_for("service_question.index"))
        if form.validate_on_submit():
            service_question_service.update(id,
                                created_by = form.created_by.data,
                                service_id = form.service_id.data,
                                question = form.question.data,
                                user_id = form.user_id.data
                               )
            return redirect(url_for("service_question.index"))
        form.created_by.data = service_question.created_by
        form.service_id.data = service_question.service_id
        form.question.data = service_question.question
        form.user_id.data = service_question.user_id
        return render_template("admin/service_question/edit.html", form=form, id=id)


    def status(self, id):
        service_question_service.status(id)
        return redirect(url_for("service_question.index"))
        pass
    