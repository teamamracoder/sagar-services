from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired


class CreateServiceForm(FlaskForm):
    service_type_id = SelectField("Service Type", validators=[DataRequired()])
    service_name = StringField("Service Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    service_charge = FloatField("Service Charge", validators=[DataRequired()])
    available_area_pincodes = StringField("Available Pincode(use comma separated)", validators=[DataRequired()])
    payment_methods = SelectMultipleField("Payment Methods", validators=[DataRequired()], coerce=int)
    discount = FloatField("Discount")
    service_img_urls = MultipleFileField("Images")

class UpdateServiceForm(FlaskForm):
    service_type_id = SelectField("Service Type", validators=[DataRequired()])
    service_name = StringField("Service Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    service_charge = FloatField("Service Charge", validators=[DataRequired()])
    available_area_pincodes = StringField("Available Pincode(use comma separated)", validators=[DataRequired()])
    payment_methods = SelectMultipleField("Payment Methods", validators=[DataRequired()], coerce=int)
    discount = FloatField("Discount")
    service_img_urls = MultipleFileField("Image [Selecting image or images will add with previous images]")


class AddServiceImageForm(FlaskForm):
    service_img_urls = MultipleFileField("Image",validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif'])])






   