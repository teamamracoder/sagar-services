from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQuestionForm, UpdateProductQuestionForm
from app.services import ProductQuestionService,ProductAnswerService, ProductService
from datetime import datetime
from app.auth import get_current_user

class ProductQuestionController:
    def __init__(self) -> None:
        self.product_question_service = ProductQuestionService()
        self.product_answer_service = ProductAnswerService()
        self.product_service = ProductService()

    def get(self):
        return render_template("admin/product_question/index.html")

    def get_product_question_data(self):
        columns = ["id", "question","created_by","created_at","is_active", "product_id", "user_id"]
        data = self.product_question_service.get(request, columns)
        data = self.product_service.add_product_with_this(data)
        data = self.product_answer_service.add_answer_with_this(data)
        return jsonify(data)

    def create(self):
        form = CreateProductQuestionForm()
        if form.validate_on_submit():
            self.product_question_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                question=form.question.data,
                product_id=form.product_id.data,
                user_id=get_current_user().id
            )
            return redirect(url_for("product_question.index"))
        return render_template("admin/product_question/add.html", form=form)

    def update(self, id):
        product_question = self.product_question_service.get_by_id(id)
        if product_question is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductQuestionForm(obj=product_question)
        products = self.product_service.get_active()
        form.product_id.choices = [(product.id, product.product_name) for product in products]
        if form.validate_on_submit():
            updated_data = {
                'question': form.question.data,
                'product_id': form.product_id.data,
                'updated_at': datetime.now(),
                'updated_by': get_current_user().id
            }
            self.product_question_service.update(id, **updated_data)
            return redirect(url_for("product_qna.index"))
        return render_template("admin/product_question/update.html", id=id, form=form)

    def status(self, id):
        product_question = self.product_question_service.get_by_id(id)
        if product_question is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_question_service.status(id)
        return redirect(url_for("product_question.index"))