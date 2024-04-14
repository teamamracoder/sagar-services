from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateCategoryForm, UpdateCategoryForm
from app.services import CategoryService
from datetime import datetime
from app.auth import get_current_user
from app.utils import FileUtils

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
        logged_in_user,roles=get_current_user().values()
        form = CreateCategoryForm()
        if form.validate_on_submit():
            filepath=FileUtils.save('categories',*form.category_img_url.data)
            self.category_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                category_name=form.category_name.data,
                category_img_url=filepath
            )
            return redirect(url_for("category.index"))
        return render_template("admin/category/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        category = self.category_service.get_by_id(id)
        if category is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateCategoryForm(obj=category)
        
        if form.validate_on_submit():
            # if file given
            # FileUtils.delete("static/uploads/categories/66a2e39826ac4e5c93d69261db3de266_localhost_diagnostics_and_medicine_hub_doctor_profile_php_png")
            updated_data = {
                'category_name': form.category_name.data,
                'updated_at': datetime.now(),
                'updated_by': logged_in_user.id
            }
            self.category_service.update(id, **updated_data)
            return redirect(url_for("category.index"))
        return render_template("admin/category/update.html", id=id, form=form)

    def status(self, id):
        category = self.category_service.get_by_id(id)
        if category is None:
            return {"status":"error","message":"item not found","data":None}
        is_active=self.category_service.status(id)
        if is_active:
            return {"status":"success","message":"Category Activated","data":is_active}
        return {"status":"success","message":"Category Deactivated","data":is_active}
