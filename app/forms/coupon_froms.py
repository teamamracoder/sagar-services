from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,DateField,FloatField
from wtforms.validators import DataRequired
from wtforms import FileField

class CreateCouponForm(FlaskForm):
    # created_by = IntegerField("created_by", validators=[DataRequired()])
    # updated_by = IntegerField("updated_by")
    coupon_code=StringField("coupon_code",validators=[DataRequired()])
    expiry_date=DateField("expiry_date",validators=[DataRequired()])
    discount_type=IntegerField("discount_type",validators=[DataRequired()])
    discount=FloatField("discount",validators=[DataRequired()])
   # coupon_img_url=StringField("coupon_img_url",validators=[DataRequired()])
    coupon_img_url = FileField("coupon_img_url", validators=[DataRequired()])
    count=IntegerField("count",validators=[DataRequired()])
    