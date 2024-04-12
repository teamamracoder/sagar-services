from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQnAForm, UpdateProductQnAForm
from app.services import ProductQnAService, ProductService, UserService
from datetime import datetime
from app.auth import get_current_user

class ProductQnAController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.product_qna_service = ProductQnAService()
        self.user_service = UserService()

    def get(self):
        return render_template("admin/product_qna/index.html")

    def get_product_qna_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "product_id", "question", "answer" "user_id"]
        question_data = self.product_qna_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(question_data)
        return jsonify(combined_data)

    def create(self):
        form = CreateProductQnAForm()
        if form.validate_on_submit():
            self.product_qna_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                product_id = form.product_id.data,
                question = form.question.data,
                user_id = get_current_user().id
            )
            return redirect(url_for("product_qna.index"))
        return render_template("admin/product_qna/add.html", form=form)

    def update(self, id):
        qna = self.product_qna_service.get_by_id(id)
        if qna is None:
            return render_template("admin/error/something_went_wrong.html")

        product=self.product_service.get_by_id(qna.product_id)
        form = UpdateProductQnAForm(obj=qna)
        form.product_id.choices = [(product.id, product.product_name)]
        if form.validate_on_submit():
            self.product_qna_service.update(
                id=id,
                updated_by=get_current_user().id,
                updated_at=datetime.now(),
                product_id=form.product_id.data,
                question=form.question.data,
                answer=form.answer.data,
            )
            return redirect(url_for("product_qna.index"))
        return render_template("admin/product_qna/update.html",form=form,id=id)
        
    def status(self, id):
        product_qna = self.product_qna_service.get_by_id(id)
        if product_qna is None:
            return render_template("admin/error/something_went_wrong.html")
        is_active=self.product_qna_service.status(id)
        if is_active:
            return {"status":"success","message":"Category Activated","data":is_active}
        return {"status":"success","message":"Category Deactivated","data":is_active}

       