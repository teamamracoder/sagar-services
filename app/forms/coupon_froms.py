from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,DateField,FloatField, SelectField
from wtforms.validators import DataRequired
from wtforms import FileField

class CreateCouponForm(FlaskForm):
    coupon_code=StringField("coupon_code",validators=[DataRequired()])
    expiry_date=DateField("expiry_date",validators=[DataRequired()])
    discount_type=SelectField("discount_type",coerce=int, validators=[DataRequired()])
    discount=FloatField("discount",validators=[DataRequired()])
    coupon_img_url = FileField("coupon_img_url")
    count=IntegerField("count",validators=[DataRequired()])
    

class UpdateCouponForm(FlaskForm):
    coupon_code=StringField("coupon_code",validators=[DataRequired()])
    expiry_date=DateField("expiry_date",validators=[DataRequired()])
    discount_type=SelectField("discount_type",coerce=int,validators=[DataRequired()])
    discount=FloatField("discount",validators=[DataRequired()])
    coupon_img_url = FileField("coupon_img_url")
    count=IntegerField("count",validators=[DataRequired()])
    