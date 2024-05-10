from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,FloatField, SelectField, DateTimeLocalField
from wtforms.validators import DataRequired
from wtforms import FileField
from flask_wtf.file import FileAllowed, FileRequired

class CreateCouponForm(FlaskForm):
    coupon_code=StringField("Coupon Code",validators=[DataRequired()])
    expiry_date=DateTimeLocalField("Expiry Date",validators=[DataRequired()])
    discount=FloatField("Discount",validators=[DataRequired()])
    discount_type=SelectField("Discount Type",coerce=int, validators=[DataRequired()])
    coupon_img_url = FileField("Image",validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif'])])
    count=IntegerField("Count",validators=[DataRequired()])
    

class UpdateCouponForm(FlaskForm):
    coupon_code=StringField("Coupon Code",validators=[DataRequired()])
    expiry_date=DateTimeLocalField("Expiry Date",validators=[DataRequired()])
    discount_type=SelectField("Discount Type",coerce=int,validators=[DataRequired()])
    discount=FloatField("Discount",validators=[DataRequired()])
    coupon_img_url = FileField("Image (Selecting an Image will replace the previous Image)")
    count=IntegerField("Count",validators=[DataRequired()])
    