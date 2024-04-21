from flask import Blueprint
from app.controllers import ProductController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
from urllib.parse import unquote

product_bp = Blueprint("product", __name__)
product_controller = ProductController()

    
@product_bp.route("/admin/products/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return product_controller.get()

@product_bp.route("/admin/products/data")
def get_product_data():
    return product_controller.get_product_data()

@product_bp.route("/admin/products/total_price")
def get_total_price():
    return product_controller.get_total_price()

@product_bp.route("/admin/products/available_pincodes")
def get_available_pincodes():
    return product_controller.get_available_pincodes()


@product_bp.route("/admin/products/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return product_controller.create()


@product_bp.route("/admin/products/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return product_controller.update(id)


@product_bp.route("/admin/products/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return product_controller.status(id)

@product_bp.route("/admin/products/details/<int:id>", methods=["GET"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def details(id):
    return product_controller.details(id)

@product_bp.route("/admin/products/addimage/<int:product_id>", methods=["GET","POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def addImage(product_id):
    return product_controller.addImage(product_id)


@product_bp.route("/admin/products/deleteImage/<int:product_id>/<path:filename>")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def deleteImage(product_id,filename):
    filename = unquote(filename)
    return product_controller.deleteImage(product_id,filename)




## customer routes ##

@product_bp.route("/products/")
def products_page():
    return product_controller.products_page()

@product_bp.route("/products/data/")
def products_page_data():
    return product_controller.products_page_data()

@product_bp.route("/product_details/<int:product_id>", methods=["GET", "PATCH"])
def product_details_page(product_id):
    return product_controller.product_details_page(product_id)