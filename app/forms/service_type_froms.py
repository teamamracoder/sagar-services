from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired


class CreateServiceTypeForm(FlaskForm):
    type_name = StringField("Service Type Name", validators=[DataRequired()])
    service_type_img_url = FileField("Service Img Url")



class UpdateServiceTypeForm(FlaskForm):
    type_name = StringField("Service Type Name", validators=[DataRequired()])
    service_type_img_url = FileField("Service Img Url")