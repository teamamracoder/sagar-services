from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, URL

class CreateMessageForm(FlaskForm):
    message=StringField("Message text",validators=[DataRequired()])
    attachement_url = FileField("📂")

class UpdateMessageForm(FlaskForm):
    message=StringField("Message text",validators=[DataRequired()])
    attachement_url = FileField("📂")