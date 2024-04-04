from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQuestionForm, UpdateProductQuestionForm
from app.services import ProductAnswerService, ProductQuestionService, ProductService
from datetime import datetime
from app.auth import get_current_user
class ProductQuestionController:
    def __init__(self) -> None:
        self.product_question_service = ProductQuestionService()
        self.product_service = ProductService()
        self.product_answer_service = ProductAnswerService()

    def get(self):
        return render_template("admin/product_question/index.html")

    def get_product_question_data(self):
        columns = ["id", "question","created_by","created_at","updated_by","updated_by","is_active", "product_id"]
        data = self.product_question_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(data)
        return jsonify(combined_data)

    def create(self):
        form = CreateProductQuestionForm()
        if form.validate_on_submit():
            question=self.product_question_service.create(
                created_by=1,
                created_at=datetime.now(),
                question=form.question.data,
                product_id=form.product_id.data,
                user_id=1
            )
            self.product_answer_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                answer=" ",
                staff_id=1,
                question_id=question.id
            )
            return redirect(url_for("product_question.index"))
            # return render_template("admin/product_question/add.html", form=form, error="product_question already exists")
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