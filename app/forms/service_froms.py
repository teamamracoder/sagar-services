from flask_wtf import FlaskForm
from wtforms.fields import *
# from wtforms import StringField, FloatField, IntegerField, FieldList
from wtforms.validators import DataRequired

# from flask_wtf.file import FileField, FileAllowed

from wtforms import Field
from wtforms.widgets import TextInput
from wtforms.validators import ValidationError


class StringArrayField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return ', '.join(str(x) for x in self.data)
        else:
            return ''

    def process_formdata(self, valuelist):
        try:
            if valuelist:
                self.data = [x.strip() for x in valuelist[0].split(',')]
            else:
                self.data = []
        except ValueError:
            raise ValidationError('Invalid input for StringArrayField')


class IntegerArrayField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return ', '.join(str(x) for x in self.data)
        else:
            return ''

    def process_formdata(self, valuelist):
        try:
            if valuelist:
                self.data = [int(x.strip()) for x in valuelist[0].split(',')]
            else:
                self.data = []
        except ValueError:
            raise ValidationError('Invalid input for IntegerArrayField')


class CreateServiceForm(FlaskForm):
    created_by= IntegerField("created_by Id", validators=[DataRequired()])
    service_name = StringField("Service Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    service_charge = FloatField("Service Charge", validators=[DataRequired()])
    available_area_pincode = IntegerArrayField("Available Area Pincode", validators=[DataRequired()])
    payment_methods = IntegerArrayField("Payment Methods", validators=[DataRequired()])
    discount = FloatField("Discount", validators=[DataRequired()])
    # service_img_urls = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    service_img_urls = StringArrayField("Service img urls", validators=[DataRequired()])
    service_type_id = IntegerField("Service type id", validators=[DataRequired()])


class UpdateServiceForm(FlaskForm):
    created_by= IntegerField("created_by Id", validators=[DataRequired()])
    service_name = StringField("Service Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    service_charge = FloatField("Service Charge", validators=[DataRequired()])
    available_area_pincode = IntegerArrayField("Available Area Pincode", validators=[DataRequired()])
    payment_methods = IntegerArrayField("Payment Methods", validators=[DataRequired()])
    discount = FloatField("Discount", validators=[DataRequired()])
    # service_img_urls = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    service_img_urls = StringArrayField("Service img urls",validators=[DataRequired()])
    service_type_id = IntegerField("Service type id", validators=[DataRequired()])









   