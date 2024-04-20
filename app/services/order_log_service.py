from app.models import OrderLogModel
from .base_service import BaseService
from app.constants import order_statuses

class OrderLogService(BaseService):
    def __init__(self) -> None:
        super().__init__(OrderLogModel)

    def get_order_log_by_order_id(self,order_id):
        order_logs= self.model.query.filter_by(order_id=order_id).order_by(self.model.created_at).all()
        order_logs_dicts = []
        for log in order_logs:
            log_dict = {
                'id': log.id,
                'order_id': log.order_id,
                'created_at': log.created_at,  # Convert datetime to string
                'status_name': order_statuses.get_value(log.order_status)  # Add your additional key and value here
            }
            order_logs_dicts.append(log_dict)

        return order_logs_dicts
    
    def add_order_log_with_this(self, items: dict) -> dict:
        for item in items["data"]:
            item["order_logs"] = self.get_order_log_by_order_id(item['id'])
        return items
    
    # def get_order_log_by_order(self,order_id):
    #     return self.model.query.filter_by(id=order_id).all()