from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired


class CreateServiceTypeForm(FlaskForm):
    created_by = IntegerField("created_by Id", validators=[DataRequired()])
    type_name = StringField("Service Type Name", validators=[DataRequired()])
    service_img_url = FileField("Service_img_url")



class UpdateServiceTypeForm(FlaskForm):
    created_by = IntegerField("created_by Id", validators=[DataRequired()])
    type_name = StringField("Service Type Name", validators=[DataRequired()])
    service_img_url = FileField("Service_img_url")