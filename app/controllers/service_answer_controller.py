from flask import render_template, redirect, url_for
from app.forms import CreateServiceAnswerForm
from app.services import ServiceAnswerService

service_answer_service = ServiceAnswerService()


class ServiceAnswerController:

    def create(self):
        form = CreateServiceAnswerForm()
        if form.validate_on_submit():
            service_answer_service.create(
                created_by =  form.created_by.data,
                question_id =  form.question_id.data,
                answer =  form.answer.data,
                staff_id =  form.staff_id.data
                )
            return redirect(url_for("service_answer.index"))
        return render_template("admin/service_answer/add.html", form=form)

    def get(self):
        service_answers = service_answer_service.get()
        return render_template("admin/service_answer/index.html", service_answers=service_answers)

    def update(self, id):
        form = CreateServiceAnswerForm()
        service_answer = service_answer_service.get_by_id(id)
        if not service_answer:
            # Handle case where service_answer doesn't exist
            return redirect(url_for("service_answer.index"))
        if form.validate_on_submit():
            service_answer_service.update(id,
                                created_by = form.created_by.data,
                                question_id = form.question_id.data,
                                answer = form.answer.data,
                                staff_id = form.staff_id.data
                               )
            return redirect(url_for("service_answer.index"))
        form.created_by.data = service_answer.created_by
        form.question_id.data = service_answer.question_id
        form.answer.data = service_answer.answer
        form.staff_id.data = service_answer.staff_id
        return render_template("admin/service_answer/edit.html", form=form, id=id)


    def status(self, id):
        service_answer_service.status(id)
        return redirect(url_for("service_answer.index"))
        pass