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
from app.services import OrderLogService

class OrderController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.order_service = OrderService()
        self.user_service = UserService()
        self.order_log_service = OrderLogService()

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
                order_status=1,
                shipping_address=form.shipping_address.data,
                payment_status=form.payment_status.data,
                area_pincode=form.area_pincode.data,
                expected_delivery=form.expected_delivery.data
            )
            ordered_product=self.product_service.get_by_id(order.product_id)
            stock=ordered_product.stock-form.quantity.data
            self.product_service.update(ordered_product.id, stock=stock)
            # insert status in order_log
            self.order_log_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                order_id=order.id,
                order_status=order.order_status
            )
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
                'shipping_address': form.shipping_address.data,
                'area_pincode': form.area_pincode.data,
                'updated_at': datetime.now(),
                'updated_by': logged_in_user.id,
                'expected_delivery':form.expected_delivery.data
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
        logged_in_user,roles=get_current_user().values()
        order = self.order_service.get_by_id(id)
        if order is None:
            return {"status":"error","message":"Order Not Found"}
        else:
            # print(status_type)
            if status_type == 'payment':
                status_key = payment_statuses.get_key(status)
                updated_data = {
                    'payment_status': status_key,
                    'updated_at': datetime.now(),
                    'updated_by': 1
                }
                return {"status":"success","message":f"{status_type} status chaged to {status}","data":status}

            if status_type == 'order':
                order_new_status = order_statuses.get_key(status)
                # get previous order status
                order_prev_status=order.order_status
                order_prev_status_name = order_statuses.get_value(order_prev_status)
                if order_prev_status!=5 and order_prev_status!=6:
                    if order_new_status>=order_prev_status :
                    # if new status is less than previous status, than can not change
                    # if order status is 'delivered','cancelled' than can not change
                        # update order table
                        updated_data = {
                            'order_status': order_new_status,
                            'updated_at': datetime.now(),
                            'updated_by': 1
                        }
                        self.order_service.update(id, **updated_data)
                        # insert status in order_log
                        self.order_log_service.create(
                            created_by=logged_in_user.id,
                            created_at=datetime.now(),
                            order_id=order.id,
                            order_status=order_new_status
                        )
                        return {"status":"success","message":f"{status_type} status chaged to {status}","data":status}
                    else:
                        return {"status":"error","message":f"{status_type} status can not be changed to old step","data":status}
                else:
                    return {"status":"error","message":f"{status_type} is already {order_prev_status_name} so, can not change status","data":status}

            else:
                return {"status":"error","message":f"{status_type} status can not be chaged","data":status}


    def details(self,id):
        order=self.order_service.get_by_id(id)
        order_logs= self.order_log_service.get_order_log_by_order_id(id)
        return render_template("admin/order/details.html",order=order,order_logs=order_logs)
    


    ## customer controllers ##

    def orders_page(self):
        columns = ['id','product_id','quantity','price','payment_method','shipping_address','payment_status','expected_delivery']
        return render_template("customer/my_orders.html")
    
    def orders_page_data(self):
        logged_in_user,roles=get_current_user().values()
        columns = ['id','product_id','created_at','quantity','price','payment_method','shipping_address','payment_status','expected_delivery','order_status']
        data = self.order_service.get_orders_by_user_id(logged_in_user.id,request,columns)
        data = self.product_service.add_product_with_this(data)
        data = self.order_service.add_order_status_with_this(data)
        data = self.order_service.add_payment_status_with_this(data)
        data = self.order_service.add_payment_method_with_this(data)
        data = self.order_log_service.add_order_logs_with_this(data)
        return jsonify(data)
    
    def cancel(self,order_id):
        order = self.order_service.get_by_id(order_id)
        order_prev_status=order.order_status
        if order_prev_status == 1 or order_prev_status ==2: 
            self.order_status(order_id,'order','CANCELLED')
        return redirect(url_for("order.orders_page"))
