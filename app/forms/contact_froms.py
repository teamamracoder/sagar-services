from flask_wtf import FlaskForm
from wtforms import StringField,FileField,TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed,MultipleFileField


class CreateContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    query_message=TextAreaField("Query Message",validators=[DataRequired()])
    query_img_urls=MultipleFileField("Query Images", validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif'])])


class UpdateContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    query_message=StringField("Query Message",validators=[DataRequired()])
    query_img_urls=FileField("Query Images")