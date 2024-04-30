from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateServiceForm, UpdateServiceForm, CreateServiceReviewForm, CreateServiceQnAForm, AddServiceImageForm
from app.services import ServiceService, ServiceTypeService, ServiceReviewService, ServiceQnAService, UserService
from datetime import datetime
from app.constants import payment_methods
from app.auth import get_current_user
from app.utils import FileUtils


class ServiceController:
    def __init__(self) -> None:
        self.service_service = ServiceService()
        self.service_type_service = ServiceTypeService()
        self.service_review_service = ServiceReviewService()
        self.service_qna_service = ServiceQnAService()
        self.user_service = UserService()

    def get(self):
        return render_template("admin/service/index.html")

    def get_service_data(self):
        # Determine the column to sort by
        columns = ["id", "created_by", "created_at", "updated_by", "updated_at", "is_active", "service_name", "description", "service_charge", "available_area_pincodes", "payment_methods", "discount", "service_img_urls", "service_type_id"]
        data = self.service_service.get(request, columns)
        combined_data = self.service_type_service.add_service_type_with_services(data)
        return jsonify(combined_data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateServiceForm()
        service_types=self.service_type_service.get_active()
        form.service_type_id.choices = [(service_type.id, service_type.type_name) for service_type in service_types]
        form.payment_methods.choices = payment_methods.get_all_items()

        if form.validate_on_submit():
            filepath=FileUtils.save('services',form.service_img_urls.data)
            if isinstance(filepath,str):
                filepath=[filepath]

            pincode_string = form.available_area_pincodes.data
            pincode_list = [pin.strip() for pin in pincode_string.split(',')]
            
            self.service_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                service_name=form.service_name.data,
                service_type_id=form.service_type_id.data,
                description=form.description.data,
                service_charge=form.service_charge.data,
                available_area_pincodes=pincode_list,
                payment_methods=form.payment_methods.data,
                discount=form.discount.data,
                service_img_urls=filepath
            )
            return redirect(url_for("service.index"))
        return render_template("admin/service/add.html", form=form)



    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        service = self.service_service.get_by_id(id)
        if service is None:
            return render_template("admin/error/something_went_wrong.html")

        service_types=self.service_type_service.get_active()
        form = UpdateServiceForm(obj=service)
        form.service_type_id.choices = [(service_type.id, service_type.type_name) for service_type in service_types]
        form.payment_methods.choices = payment_methods.get_all_items()
        
        if form.validate_on_submit():
            filepath = service.service_img_urls
            print(filepath)
            print(type(filepath))
            
            new_filepath=FileUtils.save('services',form.service_img_urls.data)
            if isinstance(new_filepath,str):
                new_filepath=[new_filepath]
            all_filepath=filepath+new_filepath

            pincode_string = form.available_area_pincodes.data
            pincode_list = [pin.strip() for pin in pincode_string.split(',')]
            
            self.service_service.update(
                id=id,
                updated_by=logged_in_user.id,
                updated_at=datetime.now(),
                service_name=form.service_name.data,
                description=form.description.data,
                service_charge=form.service_charge.data,
                available_area_pincodes=pincode_list,
                payment_methods=form.payment_methods.data,
                discount=form.discount.data,
                service_img_urls=all_filepath,
                service_type_id=form.service_type_id.data,
            )
            return redirect(url_for("service.index"))
        if(service.available_area_pincodes):
            form.available_area_pincodes.data = ', '.join(service.available_area_pincodes)
        return render_template("admin/service/update.html", form=form, id=id)


    def status(self, id):
        service = self.service_service.get_by_id(id)
        if service is None:
            return {"status":"error","message":"Service not found"}
        is_active = self.service_service.status(id)
        if is_active:
            return {"status":"success","message":"Service Activated","data":is_active}
        return {"status":"success","message":"Service Deactivated","data":is_active}


    def get_total_price(self):
        service_charge_calculated_data=self.service_service.get_total_price(request)
        return jsonify(service_charge_calculated_data)
    
    def details(self,id):
        form = AddServiceImageForm()
        service=self.service_service.get_by_id(id)
        service_type = self.service_type_service.get_by_id(service.service_type_id)

        available_payment_methods=[]
        for payment_method in service.payment_methods:
            payment_method_value=payment_methods.get_value(payment_method)
            available_payment_methods.append(payment_method_value)

        available_area_pincodes=  ', '.join(service.available_area_pincodes)
        return render_template("admin/service/details.html",service=service, form=form, service_type=service_type.type_name,available_payment_methods=available_payment_methods,available_area_pincodes=available_area_pincodes)

    def addImage(self,service_id):
        service = self.service_service.get_by_id(service_id)
        form = AddServiceImageForm()
        filepath=service.service_img_urls
        new_filepath=FileUtils.save('services',form.service_img_urls.data)
        if isinstance(new_filepath,str):
            new_filepath=[new_filepath]
        all_filepath=filepath+new_filepath

        self.service_service.update(service_id, service_img_urls= all_filepath)
        return redirect(url_for("service.details",id=service_id))
    
    def deleteImage(self,service_id,filename):
        service = self.service_service.get_by_id(service_id)
        old_filepath = service.service_img_urls
        updated_filepaths=[]
        for image in old_filepath:
            if filename.strip() != "'"+image.strip()+"'" and image.strip() != "":
               updated_filepaths.append(image)
            FileUtils.delete(filename)
        self.service_service.update(service_id, service_img_urls= updated_filepaths)
        return redirect(url_for("service.details",id=service_id)) 


    # customer section
    # def service_page():
    #     service = self.service_service.get_active()
    #     return render_template("customer/base/#service_page", service=service)


    def service_details_page(self,service_id):
        logged_in_user,roles=get_current_user().values()
        reviewForm = CreateServiceReviewForm()
        qnaForm = CreateServiceQnAForm()
        service = self.service_service.get_by_id(service_id)
        service_reviews = self.service_review_service.get_review_by_service_id(service_id)

        sr=[{
            "id":service_review.id,
            "user_id":service_review.created_by
            } for service_review in service_reviews]
            
        sr=[service_review.created_by for service_review in service_reviews]

        print(sr)

        # users_id = [(service_review.id, service_review.created_by) for service_review in service_reviews]
        # user_details = []
        # for user_id, _ in users_id:
        #     user_detail = self.user_service.get_by_id(user_id)
        #     user_details.append(user_detail)


        service_qnas = self.service_qna_service.get_qna_by_service_id(service_id)
        if service is None:
            return render_template("error/something_went_wrong.html")
        return render_template("customer/service_details.html",service=service, reviewForm=reviewForm, qnaForm=qnaForm, service_reviews=service_reviews,service_qnas=service_qnas,logged_in_user=logged_in_user)
    

    def check_area_availability(self):
        print(request.form)
        service_id = request.form.get('service_id')
        pincode = request.form.get('pincode')
        service=self.service_service.get_by_id(service_id)
        available_area_pincodes = service.available_area_pincodes
        if pincode in available_area_pincodes:
            return {"is_available":True,"message":""}
        else:
            return {"is_available":False,"message":f"{service.service_name} is currently Not Avaiable in your area"}
        