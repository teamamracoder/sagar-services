from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductQnAForm, UpdateProductQnAForm
from app.services import ProductQnAService, ProductService, UserService, OrderService
from datetime import datetime
from app.auth import get_current_user

class ProductQnAController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.product_qna_service = ProductQnAService()
        self.user_service = UserService()
        self.order_service = OrderService()

    def get(self):
        return render_template("admin/product_qna/index.html")

    def get_product_qna_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "product_id", "question", "answer" "user_id"]
        question_data = self.product_qna_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(question_data)
        return jsonify(combined_data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateProductQnAForm()
        if form.validate_on_submit():
            self.product_qna_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                product_id = form.product_id.data,
                question = form.question.data,
                user_id = logged_in_user.id
            )
            return redirect(url_for("product_qna.index"))
        return render_template("admin/product_qna/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        qna = self.product_qna_service.get_by_id(id)
        if qna is None:
            return render_template("admin/error/something_went_wrong.html")

        product=self.product_service.get_by_id(qna.product_id)
        form = UpdateProductQnAForm(obj=qna)
        form.product_id.choices = [(product.id, product.product_name)]
        if form.validate_on_submit():
            self.product_qna_service.update(
                id=id,
                updated_by=logged_in_user.id,
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
            return {"status":"error","message":"QnA Not Found"}
        is_active=self.product_qna_service.status(id)
        if is_active:
            return {"status":"success","message":"QnA Activated","data":is_active}
        return {"status":"success","message":"QnA Deactivated","data":is_active}



    def product_qna_create(self,product_id):
        logged_in_user,roles=get_current_user().values()
        qnaForm = CreateProductQnAForm()
        products = self.product_service.get_active()

        if qnaForm.validate_on_submit():
            
            is_ordered = self.order_service.get_by_user_and_product_id(product_id, logged_in_user.id)
            is_qna = self.product_qna_service.get_check_is_qna_or_not(product_id, logged_in_user.id)
            
            if is_ordered:
                if is_qna is None:
                    product = self.product_qna_service.create(
                        created_by=logged_in_user.id,
                        created_at=datetime.now(),
                        product_id = qnaForm.product_id.data,
                        question = qnaForm.question.data,
                        user_id = logged_in_user.id
                    )
                    product=self.product_service.get_by_id(product_id)
                    return redirect(url_for("product.product_details_page",product_id=product_id))
                
                error_message = "Can't give ask any query..! Already done..."
                return redirect(url_for("product.product_details_page", product_id=product_id, error=error_message))

            error_message = "Can't give ask any question..! Order the product first."
            return redirect(url_for("product.product_details_page", product_id=product_id, error=error_message))

        return redirect(url_for("product.product_details_page",product_id=product_id,qnaForm=qnaForm))

       