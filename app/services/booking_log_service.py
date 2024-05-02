from app.models import BookingLogModel
from .base_service import BaseService
from app.constants import service_statuses

class BookingLogService(BaseService):
    def __init__(self) -> None:
        super().__init__(BookingLogModel)

    def get_booking_log_by_booking_id(self,booking_id):
        booking_logs= self.model.query.filter_by(booking_id=booking_id).order_by(self.model.created_at).all()
        booking_logs_dicts = []
        if booking_logs:
            for log in booking_logs:
                log_dict = {
                    'id': log.id,
                    'booking_id': log.booking_id,
                    'created_at': log.created_at,  # Convert datetime to string
                    'status_name': service_statuses.get_value(log.booking_status)  # Add your additional key and value here
                }
                booking_logs_dicts.append(log_dict)

        return booking_logs_dicts
    
    # def add_booking_log_with_this(self, items: dict) -> dict:
    #     for item in items["data"]:
    #         item["booking_logs"] = self.get_booking_log_by_booking_id(item['id'])
    #     return items
    
    # def get_booking_log_by_booking(self,booking_id):
    #     return self.model.query.filter_by(id=booking_id).all()

    def add_booking_logs_with_this(self,bookings):
        for booking in bookings['data']:
            booking_logs = self.model.query.filter_by(booking_id=booking['id']).booking_by(self.model.created_at).all()
            booking_logs_dicts = []
            if booking_logs:
                for log in booking_logs:
                    log_dict = {
                        'log_id': log.id,
                        'created_at': log.created_at,  # Convert datetime to string
                        'status_key': log.booking_status,  # Convert datetime to string
                        'status_name': service_statuses.get_value(log.service_status)  # Add your additional key and value here
                    }
                    booking_logs_dicts.append(log_dict)
                booking['booking_logs']=booking_logs_dicts
        return bookings
    
    
    def add_booking_latest_log(self,bookings):
        for booking in bookings['data']:
            booking_log= self.model.query.filter_by(booking_id=booking['id']).order_by(self.model.created_at.desc()).first()
            if booking_log:
                booking['booking_latest_log'] = {
                    'booking_log_id': booking_log.id,
                    'created_at': booking_log.created_at, 
                    'status':booking_log.booking_status,
                    'status_name': service_statuses.get_value(booking_log.booking_status)
                }
        return bookings