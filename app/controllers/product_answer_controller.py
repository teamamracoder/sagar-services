from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductAnswerForm, UpdateProductAnswerForm
from app.services import ProductAnswerService, ProductQuestionService
from datetime import datetime

class ProductAnswerController:
    def __init__(self) -> None:
        self.product_answer_service = ProductAnswerService()
        self.product_question_service = ProductQuestionService()

    def get(self):
        return render_template("admin/product_answer/index.html")

    def get_product_answer_data(self):
        columns = ["id", "answer","created_by","created_at","updated_by","updated_by","is_active", "question_id", "staff_id"]
        data = self.product_answer_service.get(request, columns)
        combined_data = self.product_question_service.add_question_with_answers(data)
        return jsonify(combined_data)

    def create(self):
        form = CreateProductAnswerForm()
        questions = self.product_question_service.get_active()
        form.question_id.choices = [(question.id, question.question) for question in questions]
        if form.validate_on_submit():
            self.product_answer_service.create(
                created_by=1,
                created_at=datetime.now(),
                answer=form.answer.data,
                staff_id=1,
                question_id=form.question_id.data
            )
            return redirect(url_for("product_answer.index"))
            # return render_template("admin/product_answer/add.html", form=form, error="product_answer already exists")
        return render_template("admin/product_answer/add.html", form=form)

    def update(self, id):
        product_answer = self.product_answer_service.get_by_id(id)
        if product_answer is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductAnswerForm(obj=product_answer)
        questions = self.product_question_service.get_active()
        form.question_id.choices = [(question.id, question.question) for question in questions]

        if form.validate_on_submit():
            updated_data = {
                'answer': form.answer.data,
                'updated_at': datetime.now(),
                'updated_by': 1,
                'question_id' : form.question_id.data
            }
            self.product_answer_service.update(product_answer.id, **updated_data)
            return redirect(url_for("product_answer.index"))
        return render_template("admin/product_answer/update.html", form=form, product_answer=product_answer)

    def status(self, id):
        product_answer = self.product_answer_service.get_by_id(id)
        if product_answer is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_answer_service.status(id)
        return redirect(url_for("product_answer.index"))