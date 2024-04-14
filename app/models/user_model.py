from db import db
from flask_login import UserMixin


class UserModel(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    created_by = db.Column(db.Integer)

    created_at = db.Column(db.DateTime)

    updated_by = db.Column(db.Integer)

    updated_at = db.Column(db.DateTime)

    is_active = db.Column(db.Boolean, default=False)

    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    address = db.Column(db.Text)
    gender = db.Column(db.String(20))
    dob = db.Column(db.Date)
    profile_photo_url = db.Column(db.Text)

    # roles = db.relationship("RoleModel", backref="user")
    # staff = db.relationship("RoleModel", back_populates="users",uselist=False)
    # conversations = db.relationship("ConversationModel", back_populates="users")
    # messages = db.relationship("MessageModel", back_populates="users")
    # products = db.relationship("ProductModel")
    # categories = db.relationship("CategoryModel")
    # product_answers = db.relationship("ProductAnswerModel", back_populates="users")
    # product_questions = db.relationship("ProductQuestionModel", back_populates="users")
    # product_reviews = db.relationship("ServiceReviewModel", back_populates="users")
    # orders = db.relationship("OrderModel", back_populates="users")
    # cart = db.relationship("CartModel", back_populates="users",uselist=False)
    # wishlist = db.relationship("WishlistModel", back_populates="users",uselist=False)
    # service = db.relationship("ServiceModel", back_populates="users")
    # service_type = db.relationship("ServiceTypeModel", back_populates="users")
    # service_answers = db.relationship("ServiceAnswerModel", back_populates="users")
    # service_questions = db.relationship("ServiceQuestionModel", back_populates="users")
    # bookings = db.relationship("BookingModel", back_populates="users")
    # service_reviews = db.relationship("ServiceReviewModel", back_populates="users")
    # coupons = db.relationship("CouponModel", back_populates="users")
