from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductAnswerForm, UpdateProductAnswerForm
from app.services import ProductAnswerService, ProductQuestionService
from datetime import datetime
from app.auth import get_current_user

class ProductAnswerController:
    def __init__(self) -> None:
        self.product_answer_service = ProductAnswerService()
        self.product_question_service = ProductQuestionService()

    def get(self):
        return render_template("admin/product_answer/index.html")

    def get_product_answer_data(self):
        columns = ["id", "answer","is_active", "question_id", "staff_id"]
        data = self.product_answer_service.get(request, columns)
        data = self.product_question_service.add_question_with_this(data)
        return jsonify(data)

    def create(self):
        form = CreateProductAnswerForm()
        if form.validate_on_submit():
            question=self.product_question_service.get_by_id(form.question_id.data)
            if question:
                answer=self.product_answer_service.get_answer_details_by_question_id(question.id)
                if not answer:
                    self.product_answer_service.create(
                        created_by=get_current_user().id,
                        created_at=datetime.now(),
                        answer=form.answer.data,
                        staff_id=get_current_user().id,
                        question_id=form.question_id.data
                    )
                    return redirect(url_for("product_question.index"))
                else:
                    return render_template("admin/product_answer/add.html", form=form, error=f"*The question has an Answer already, rather <a href='/admin/product_answers/update/{answer.id}' class='text-dark'>Edit</a> it.")
            else:
                return render_template("admin/product_answer/add.html", form=form, error="*Invalid product Question id")

        return render_template("admin/product_answer/add.html", form=form)
    

    def create_for_question(self,question_id):
        form = CreateProductAnswerForm()
        if form.validate_on_submit():
            self.product_answer_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                answer=form.answer.data,
                staff_id=get_current_user().id,
                question_id=question_id
            )
            return redirect(url_for("product_question.index"))
        return render_template("admin/product_answer/add.html", form=form, question_id=question_id)


    def update(self, id):
        product_answer = self.product_answer_service.get_by_id(id)
        if product_answer is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductAnswerForm(obj=product_answer)

        if form.validate_on_submit():
            updated_data = {
                'answer': form.answer.data,
                'updated_at': datetime.now(),
                'updated_by': get_current_user().id,
                'question_id' : form.question_id.data
            }
            self.product_answer_service.update(id, **updated_data)
            return redirect(url_for("product_question.index"))
        return render_template("admin/product_answer/update.html", id=id, form=form)

    def status(self, id):
        product_answer = self.product_answer_service.get_by_id(id)
        if product_answer is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_answer_service.status(id)
        return redirect(url_for("product_question.index"))