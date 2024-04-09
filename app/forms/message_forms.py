from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, TextAreaField, FieldList
from wtforms.validators import DataRequired, URL

class CreateMessageForm(FlaskForm):
    message=StringField("Message text",validators=[DataRequired()])
    

class UpdateMessageForm(FlaskForm):
    message=StringField("Message text",validators=[DataRequired()])
 