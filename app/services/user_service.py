from app.models import UserModel
from .base_service import BaseService
from db import db
from datetime import datetime, timedelta
from collections import defaultdict
from sqlalchemy import func

class UserService(BaseService):
    def __init__(self) -> None:
        super().__init__(UserModel)

    def get_user_by_email_and_password(self, email, password):
        return UserModel.query.filter_by(email=email, password=password).first()

    def add_user_with_this(self, items: dict) -> dict:
        for item in items["data"]:
            user = self.get_by_id(item["user_id"])
            item["fullname"] = user.first_name + " " + user.last_name
            item["email"] = user.email
        return items

    def get_user_name_by_this(self,user_id):
        return UserModel.query.filter_by(user_id=user_id).all()

    def add_message_with_this(self, messages: dict) -> dict:
        for message in messages:
            message.sent_by = self.get_by_id(message.created_by).first_name
        return messages

    def get_user_by_id(self,id):
        return UserModel.query.filter_by(id=id).all()


    def get_user_by_reviews_for_home(self, datas) -> dict:
        for data in datas:
            reviews = data["service_review"]
            serialized_users = []
            for review in reviews:
                users = self.get_user_by_id(review["user_id"])
                serialized_user = [self.serialize_users(user) for user in users]
                serialized_users.extend(serialized_user)
            data["serialized_users"] = serialized_users
        return datas


    def serialize_users(self, user):
        return {key: getattr(user, key) for key in user.__dict__ if not key.startswith("_")}

    def get_user_by_email(self, email):
        return UserModel.query.filter_by(email=email).first()

    def get_user_by_mobile(self, mobile):
        return UserModel.query.filter_by(mobile=mobile).first()

    def add_username_with_this(self, messages:dict):
        for message in messages:
            message["sent_by"] = self.get_by_id(message['created_by']).first_name
        return messages
    def get_users_registered_data_for_Chart(self, time_range):
        dates = []
        counts = []
        if time_range == 'Weekly':
            end_date = datetime.now()
            start_date = end_date - timedelta(days=end_date.weekday())

            current_date = start_date
            while current_date <= end_date:
                day_start = datetime.combine(current_date, datetime.min.time())
                day_end = datetime.combine(current_date, datetime.max.time())

                user_count = (
                    UserModel.query
                    .filter(UserModel.created_at >= day_start)
                    .filter(UserModel.created_at <= day_end)
                    .filter(UserModel.is_active ==True)
                    .count()
                )

                dates.append(current_date.strftime('%Y-%m-%d'))
                counts.append(user_count)
                current_date += timedelta(days=1)

        elif time_range == 'Yearly':
            current_year = datetime.now().year
            current_month = datetime.now().month
            start_date = datetime(current_year, 1, 1)
            next_month_start = datetime(current_year, current_month + 1, 1)
            end_date = next_month_start - timedelta(days=1)
            user_registrations = UserModel.query.filter(
                UserModel.created_at >= start_date,
                UserModel.created_at <= end_date,
                UserModel.is_active ==True
            ).all()
            monthly_counts = defaultdict(int)
            for registration in user_registrations:
                month_key = (registration.created_at.year, registration.created_at.month)
                monthly_counts[month_key] += 1

            for month in range(1, current_month + 1):
                first_day_of_month = datetime(current_year, month, 1)
                month_count = monthly_counts[(current_year, month)]
                date_range = f"{first_day_of_month.strftime('%B')}"
                dates.append(date_range)
                counts.append(month_count)

        elif time_range == 'Monthly':
            end_date = datetime.now()
            start_date = end_date - timedelta(days=29)


            current_date = start_date
            while current_date <= end_date:
                week_start = current_date
                week_end = min(current_date + timedelta(days=6), end_date)
                user_count = (
                    UserModel.query
                    .filter(UserModel.created_at >= week_start)
                    .filter(UserModel.created_at <= week_end + timedelta(days=1))
                    .filter(UserModel.is_active ==True)
                    .count()
                )

                dates.append(f"{week_start.strftime('%d/%m')} - {week_end.strftime('%d/%m')}")
                counts.append(user_count)

                current_date += timedelta(days=6)

        elif time_range == 'Overall':
            min_date = UserModel.query.with_entities(func.min(UserModel.created_at)).scalar()
            max_date = UserModel.query.with_entities(func.max(UserModel.created_at)).scalar()
            start_year = min_date.year if min_date else datetime.now().year
            end_year = max_date.year if max_date else datetime.now().year

            yearly_counts = defaultdict(int)
            for year in range(start_year, end_year + 1):
                orders = UserModel.query.filter(
                    func.extract('year', UserModel.created_at) == year,
                    UserModel.is_active == True
                ).all()
                yearly_counts[year] = len(orders)
            for year in range(start_year, end_year + 1):
                dates.append(str(year))
                counts.append(yearly_counts[year])

        dataset = {
            "label": dates,
            "data": counts
        }

        return dataset

    def get_active(self):
        return self.model.query.filter_by(is_active=True).count()

    def get_all_users(self,time_range):
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
               total_users = UserModel.query.filter(
                   UserModel.created_at >= start_date,
                   UserModel.created_at <= end_date,
                   UserModel.is_active == True
               ).count()
           else:
               total_users = UserModel.query.filter(
                   UserModel.is_active == True
               ).count()

           return total_users
    
    def check_coupon_by_coupon_id(self,user_id,coupon_id):
        user = self.get_by_id(user_id)
        if user.coupon==coupon_id:
            return True
        else:
            return False
        
    def delete_coupon(self,user_id,coupon_id):
        user = self.model.query.filter_by(id=user_id).first()
        print(user.coupon)
        user.coupon =None
        db.session.commit()

