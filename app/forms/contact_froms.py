from flask_wtf import FlaskForm
from wtforms import StringField,FileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed, FileRequired


class CreateContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    query_message=StringField("Query Message",validators=[DataRequired()])
    query_img_urls=FileField("Query Images", validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif'])])


class UpdateContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    query_message=StringField("Query Message",validators=[DataRequired()])
    query_img_urls=FileField("Query Images")