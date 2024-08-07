from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class CreateBookingForm(FlaskForm):
    service_id  = SelectField('Service', validators=[DataRequired()])
    total_charges = FloatField('Total Charges')
    service_location = TextAreaField('Service Location', validators=[DataRequired()])
    service_status = SelectField('Service Status', coerce=int, validators=[DataRequired()])
    payment_status = SelectField('Payment Status', coerce=int, validators=[DataRequired()])
    payment_method = SelectField('Payment Method', coerce=int, validators=[DataRequired()])
    area_pincode  = StringField("Available Pincode", validators=[DataRequired()])

class UpdateBookingForm(FlaskForm):
    service_id  = SelectField('Service', validators=[DataRequired()])
    staff_id  = SelectField("Select a Staff")
    total_charges = FloatField('Total Charges')
    service_location = TextAreaField('Service Location', validators=[DataRequired()])
    service_status = SelectField('Service Status', coerce=int, validators=[DataRequired()])
    payment_status = SelectField('Payment Status', coerce=int, validators=[DataRequired()])
    payment_method = SelectField('Payment Method', coerce=int, validators=[DataRequired()])
    area_pincode = StringField("Available Pincode", validators=[DataRequired()])
    booking_details = TextAreaField("Extra Charges [booking details]")
