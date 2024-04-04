from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQnAForm, UpdateProductQnAForm
from app.services import ProductAnswerService, ProductQuestionService, ProductService
from datetime import datetime
from app.auth import get_current_user

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
        data = self.product_service.add_product_with_this(data)
        data = self.product_answer_service.add_product_question_with_answer(data)
        return jsonify(data)
    

    def create(self):
        form = CreateProductQnAForm()
        if form.validate_on_submit():
            question = self.product_question_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                question=form.question.data,
                product_id=form.product_id.data,
                user_id=form.user_id.data
            )
            self.product_answer_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                answer=form.answer.data,
                staff_id=get_current_user().id,
                question_id=question.id
            )
            return redirect(url_for("product_qna.index"))
        return render_template("admin/product_qna/add.html", form=form)
    
    def update(self,id):
        form = UpdateProductQnAForm()
        question=self.product_question_service.get_by_id(id)
        answer=self.product_answer_service.get_answer_details_by_question_id(id)

        product = self.product_service.get_by_id(question.product_id)
        form.product_id.choices = [(product.id, product.product_name)]

        if form.validate_on_submit():
            question = self.product_question_service.update(
                id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                question=form.question.data,
                product_id=form.product_id.data,
                user_id=form.user_id.data
            )
            self.product_answer_service.update(
                answer.id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                answer=form.answer.data,
                staff_id=get_current_user().id,
                question_id=question.id
            )
            return redirect(url_for("product_qna.index"))
        return render_template("admin/product_qna/update.html", id=id, form=form, answer=answer,question=question)

    def status(self, id):
        product_question = self.product_question_service.get_by_id(id)
        if product_question is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_question_service.status(id)
        return redirect(url_for("product_qna.index"))