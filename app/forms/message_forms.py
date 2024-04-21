from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class CreateMessageForm(FlaskForm):
    message=StringField("Message text",validators=[DataRequired()])
    attachement_url = FileField("📂",validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif','pdf','docx','xlxs'])])

class UpdateMessageForm(FlaskForm):
    message=StringField("Message text",validators=[DataRequired()])
    attachement_url = FileField("📂")