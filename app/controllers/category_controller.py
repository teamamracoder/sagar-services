from flask import render_template, redirect, url_for, request
from app.forms import CreateCategoryForm
from app.forms import UpdateCategoryForm
from app.services import CategoryService
from datetime import datetime
category_service = CategoryService()


class CategoryController:

    def create(self):
        form = CreateCategoryForm()
        if form.validate_on_submit():
            if category_service.create(
                category_name=form.category_name.data,
                created_by=1,
                created_at=datetime.now(),
                category_img_url=form.category_img_url.data
            ):
                return redirect(url_for("category.index"))
            return render_template("admin/category/add.html", form=form,error="category already exist")
        return render_template("admin/category/add.html", form=form)

    def get(self):
        categories = category_service.get()
        return render_template("admin/category/index.html", categories=categories)

    def update(self,id):
        form = UpdateCategoryForm()
        category=category_service.get_category_by_id(id)
        if category is None:
            return render_template("admin/error/something_went_wrong.html")
        if form.validate_on_submit():
            category_service.update(
                id,
                category_name=form.category_name.data,
                updated_by=1,
                updated_at=datetime.now(),
                category_img_url=form.category_img_url.data
            )
            return redirect(url_for("category.index"))
        form.category_name.data=category.category_name
        form.category_img_url.data=category.category_img_url
        return render_template("admin/category/update.html",id=id, form=form)

    def status(self,id):
        category = category_service.get_category_by_id(id)
        if category is None:
            return render_template("admin/error/something_went_wrong.html")
        category_service.status(id)
        return redirect(url_for("category.index"))
