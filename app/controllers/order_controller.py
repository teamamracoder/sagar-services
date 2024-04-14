from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateOrderForm,UpdateOrderForm
from app.services import ProductService
from app.services import OrderService
from datetime import datetime
from app.constants import payment_methods
from app.constants import order_statuses
from app.constants import payment_statuses
from app.services import UserService
from app.auth import get_current_user

class OrderController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.order_service = OrderService()
        self.user_service = UserService()

    def get(self):
        return render_template("admin/order/index.html")

    def get_order_data(self):
        columns = ["id", "product_id", "user_id","quantity","price","payment_method","order_status","shipping_address","payment_status","area_pincode","created_by","created_at","updated_by","updated_at","is_active"]
        data = self.order_service.get(request, columns)
        data = self.product_service.add_product_with_this(data)
        data = self.user_service.add_user_with_this(data)
        data = self.order_service.add_payment_method_with_this(data)
        data = self.order_service.add_order_status_with_this(data)
        data = self.order_service.add_payment_status_with_this(data)
        return jsonify(data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateOrderForm()
        form.payment_method.choices = payment_methods.get_all_items()
        form.order_status.choices = order_statuses.get_all_items()
        form.payment_status.choices = payment_statuses.get_all_items()
        
        if form.validate_on_submit():
            order=self.order_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                product_id=form.product_id.data,
                user_id=form.user_id.data,
                quantity=form.quantity.data,
                price=form.price.data,
                payment_method=form.payment_method.data,
                order_status=form.order_status.data,
                shipping_address=form.shipping_address.data,
                payment_status=form.payment_status.data,
                area_pincode=form.area_pincode.data,
            )
            ordered_product=self.product_service.get_by_id(order.product_id)
            stock=ordered_product.stock-1
            self.product_service.update(ordered_product.id, stock=stock)
            return redirect(url_for("order.index"))
        return render_template("admin/order/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        order = self.order_service.get_by_id(id)
        if order is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateOrderForm(obj=order)

        product = self.product_service.get_by_id(order.product_id)
        form.product_id.choices = [(product.id, product.product_name)]

        form.payment_method.choices = payment_methods.get_all_items()
        form.order_status.choices = order_statuses.get_all_items()
        form.payment_status.choices = payment_statuses.get_all_items()
        if form.validate_on_submit():
            updated_data = {
                'product_id': form.product_id.data,
                'user_id': form.user_id.data,
                'quantity': form.quantity.data,
                'price': form.price.data,
                'payment_method': form.payment_method.data,
                'order_status': form.order_status.data,
                'shipping_address': form.shipping_address.data,
                'payment_status': form.payment_status.data,
                'area_pincode': form.area_pincode.data,
                'updated_at': datetime.now(),
                'updated_by': logged_in_user.id
            }
            self.order_service.update(id, **updated_data)
            return redirect(url_for("order.index"))
        
        return render_template("admin/order/update.html", id=id, form=form)

    def status(self, id):
        order = self.order_service.get_by_id(id)
        if order is None:
            return {"status":"error","message":"Order Not Found"}
        is_active=self.order_service.status(id)
        if is_active:
            return {"status":"success","message":"Order Activated","data":is_active}
        return {"status":"success","message":"Order Deactivated","data":is_active}

    def order_status(self,id,status_type,status):
        order = self.order_service.get_by_id(id)
        if order is None:
            return {"status":"error","message":"Order Not Found"}
        if status_type == 'payment':
            status_key = payment_statuses.get_key(status)
            updated_data = {
                'payment_status': status_key,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
        if status_type == 'order':
            status_key = order_statuses.get_key(status)
            updated_data = {
                'order_status': status_key,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
        self.order_service.update(id, **updated_data)
        return {"status":"success","message":f"{status_type} status chaged to {status}","data":status}

    def details(self,id):
        order=self.order_service.get_by_id(id)
        return render_template("admin/order/details.html",order=order)