from flask import render_template, redirect, url_for
from app.forms import CreateCategoryForm
from app.services import CategoryService

category_service = CategoryService()


class CategoryController:

    def create(self):
        form = CreateCategoryForm()
        if form.validate_on_submit():
            category_service.create(form.category.data)
            return redirect(url_for("category_bp.index"))
        return render_template("admin/category/add.html", form=form)

    def get(self):
        categories = category_service.get()
        return render_template("admin/category/index.html", categories=categories)
