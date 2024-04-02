from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateCategoryForm, UpdateCategoryForm
from app.services import CategoryService
from datetime import datetime

class CategoryController:
    def __init__(self) -> None:
        self.category_service = CategoryService()

    def get(self):
        return render_template("admin/category/index.html")

    def get_category_data(self):
        columns = ["id", "category_name","created_by","created_at","updated_by","updated_by","is_active"]
        data = self.category_service.get(request, columns)
        return jsonify(data)

    def create(self):
        form = CreateCategoryForm()
        if form.validate_on_submit():
            self.category_service.create(
                created_by=1,
                created_at=datetime.now(),
                category_name=form.category_name.data,
            )
            return redirect(url_for("category.index"))
            # return render_template("admin/category/add.html", form=form, error="category already exists")
        return render_template("admin/category/add.html", form=form)

    def update(self, id):
        category = self.category_service.get_by_id(id)
        if category is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateCategoryForm(obj=category)
        
        if form.validate_on_submit():
            updated_data = {
                'category_name': form.category_name.data,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
            self.category_service.update(category.id, **updated_data)
            return redirect(url_for("category.index"))
        return render_template("admin/category/update.html", form=form, category=category)

    def status(self, id):
        category = self.category_service.get_by_id(id)
        if category is None:
            return render_template("admin/error/something_went_wrong.html")
        self.category_service.status(id)
        return redirect(url_for("category.index"))