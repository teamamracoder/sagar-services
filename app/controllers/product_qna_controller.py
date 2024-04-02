from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQnAForm, UpdateProductQnAForm
from app.services import ProductAnswerService, ProductQuestionService, ProductService
from datetime import datetime

class ProductQnAController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.product_answer_service = ProductAnswerService()
        self.product_question_service = ProductQuestionService()

    def get(self):
        return render_template("admin/product_qna/index.html")

    # based on question
    def get_product_qna_data(self):
        columns = ["id", "question","created_by","created_at","is_active", "product_id"]
        data = self.product_question_service.get(request, columns)
        product_combined_data = self.product_service.add_product_with_questions(data)
        qna_data = self.product_answer_service.add_product_question_with_answer(data)
        return jsonify(qna_data)
    

    def create(self):
        form = CreateProductQnAForm()
        products=self.product_service.get_active()
        form.product_id.choices = [(product.id, product.product_name) for product in products]
        if form.validate_on_submit():
            question=self.product_question_service.create(
                created_by=1,
                created_at=datetime.now(),
                question=form.question.data,
                product_id=form.product_id.data,
                user_id=1
            )
            self.product_answer_service.create(
                created_by=1,
                created_at=datetime.now(),
                answer=form.answer.data,
                staff_id=1,
                question_id=question.id
            )
            return redirect(url_for("product_qna.index"))
            # return render_template("admin/product_answer/add.html", form=form, error="product_answer already exists")
        return render_template("admin/product_qna/add.html", form=form)

    def status(self, id):
        product_question = self.product_question_service.get_by_id(id)
        if product_question is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_question_service.status(id)
        return redirect(url_for("product_qna.index"))