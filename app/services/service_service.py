from app.models import ServiceModel
from .base_service import BaseService
from datetime import datetime, timedelta

class ServiceService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceModel)

    def add_service_with_this(self, datas):
        for data in datas["data"]:
            service_name = self.get_service_by_id(data["service_id"])
            if service_name:
                data["service_name"] = service_name
            else:
                # Handle case where service with the given ID doesn't exist
                data["service_name"] = "Unknown"
        return datas

    def get_service_name_by_id(self,service_id):
        return ServiceModel.query.filter_by(id=service_id).first().service_name

    def get_active(self):
        return ServiceModel.query.filter_by(is_active=True).order_by(ServiceModel.service_name).all()

    def get_total_price(self,request):
        service_id = int(request.args.get("service_id"))

        service=self.get_by_id(service_id)
        if service is None:
            return {"error": "Product not found"}

        discount=service.discount
        service_charge=service.service_charge
        total_charge=float((service_charge - discount))

        service_charge_calculated_data={
            'service_id' : service_id,
            'service_charge' : service_charge,
            'discount' : discount,
            'total_charge' : total_charge
        }
        return service_charge_calculated_data

    def get_service_by_id(self, id):
        service = ServiceModel.query.filter_by(id=id).first()
        if service:
            return service.service_name
        else:
            return None  # or raise an exception depending on your use case


    # my_booking
    def get_service_name_by_booking_id(self, service_id):
        service = self.model.query.filter_by(id=service_id).first()
        if service:
            return service.service_name
        else:
            return None

    def serialized_product_services(self, services_item):
        if services_item:
            serialized_services_item = {key: getattr(services_item, key) for key in services_item.__dict__.keys() if not key.startswith("_")}
            return serialized_services_item
        else:
            return None

    def get_all_services(self,time_range):
           end_date = datetime.now()
           if time_range == 'Weekly':
               start_date = end_date - timedelta(days=end_date.weekday())
           elif time_range == 'Monthly':
               start_date = end_date.replace(day=1)- timedelta(days=1)
           elif time_range == 'Yearly':
               start_date = end_date.replace(month=1, day=1)
           elif time_range == 'Overall':
               start_date = None

           if start_date is not None:
               total_services = ServiceModel.query.filter(
                   ServiceModel.created_at >= start_date,
                   ServiceModel.created_at <= end_date,
                   ServiceModel.is_active == True
               ).count()
           else:
               total_services = ServiceModel.query.filter(
                   ServiceModel.is_active == True
               ).count()

           return total_services