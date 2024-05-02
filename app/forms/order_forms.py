from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired

class CreateOrderForm(FlaskForm):
    product_id  = IntegerField('Product Id', validators=[DataRequired()])
    user_id  = IntegerField("User Id", validators=[DataRequired()])
    quantity  = IntegerField("Quantity", validators=[DataRequired()], default=1)
    price  = FloatField("Price", validators=[DataRequired()])
    payment_method  = SelectField('Select Payment Method', coerce=int, validators=[DataRequired()])
    # order_status  = SelectField('order_status', coerce=int, validators=[DataRequired()])
    shipping_address  = TextAreaField("Shipping Address", validators=[DataRequired()])
    mobile = StringField('Mobile No.', validators=[DataRequired()])
    payment_status  = SelectField('Select Payment Status', coerce=int, validators=[DataRequired()])
    area_pincode  = StringField("Area Pincode", validators=[DataRequired()])
    expected_delivery = DateField("Expected Delivery")

class UpdateOrderForm(FlaskForm):
    product_id = SelectField('Product Id',coerce=int, validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    payment_method = SelectField('Payment Method', coerce=int, validators=[DataRequired()])
    # order_status = SelectField('order_status', coerce=int, validators=[DataRequired()])
    shipping_address = TextAreaField("Shipping Address", validators=[DataRequired()])
    mobile = StringField('Mobile No.', validators=[DataRequired()])
    # payment_status = SelectField('payment_status', coerce=int, validators=[DataRequired()])
    area_pincode = StringField("Area Pincode", validators=[DataRequired()])
    expected_delivery = DateField("Expected Delivery")