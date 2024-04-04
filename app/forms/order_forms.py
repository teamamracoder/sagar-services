from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class CreateOrderForm(FlaskForm):
    product_id  = SelectField('Product', coerce=int, validators=[DataRequired()])
    user_id  = IntegerField("user_id", validators=[DataRequired()])
    quantity  = IntegerField("Quantity", validators=[DataRequired()], default=1)
    price  = FloatField("Price", validators=[DataRequired()])
    payment_method  = SelectField('payment_method', coerce=int, validators=[DataRequired()])
    order_status  = SelectField('order_status', coerce=int, validators=[DataRequired()])
    shipping_address  = TextAreaField("shipping_address", validators=[DataRequired()])
    payment_status  = SelectField('payment_status', coerce=int, validators=[DataRequired()])
    area_pincode  = StringField("area_pincode", validators=[DataRequired()])

class UpdateOrderForm(FlaskForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    user_id = IntegerField("user_id", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    payment_method = SelectField('payment_method', coerce=int, validators=[DataRequired()])
    order_status = SelectField('order_status', coerce=int, validators=[DataRequired()])
    shipping_address = TextAreaField("shipping_address", validators=[DataRequired()])
    payment_status = SelectField('payment_status', coerce=int, validators=[DataRequired()])
    area_pincode = StringField("area_pincode", validators=[DataRequired()])