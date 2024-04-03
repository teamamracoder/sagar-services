from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQuestionForm, UpdateProductQuestionForm
from app.services import ProductQuestionService, ProductService
from datetime import datetime

class ProductQuestionController:
    def __init__(self) -> None:
        self.product_question_service = ProductQuestionService()
        self.product_service = ProductService()

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
            self.product_question_service.create(
                created_by=1,
                created_at=datetime.now(),
                question=form.question.data,
                product_id=2,
                user_id=1
            )
            return redirect(url_for("product_question.index"))
            # return render_template("admin/product_question/add.html", form=form, error="product_question already exists")
        return render_template("admin/product_question/add.html", form=form)

    def update(self, id):
        product_question = self.product_question_service.get_by_id(id)
        if product_question is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductQuestionForm(obj=product_question)
        
        if form.validate_on_submit():
            updated_data = {
                'question': form.question.data,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
            self.product_question_service.update(product_question.id, **updated_data)
            return redirect(url_for("product_question.index"))
        return render_template("admin/product_question/update.html", form=form, product_question=product_question)

    def status(self, id):
        product_question = self.product_question_service.get_by_id(id)
        if product_question is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_question_service.status(id)
        return redirect(url_for("product_question.index"))