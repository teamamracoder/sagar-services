from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class CreateContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    query_message=StringField("Query Message",validators=[DataRequired()])
    #query_img_urls=StringField("Query Images",validators=[DataRequired()])


class UpdateContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    query_message=StringField("Query Message",validators=[DataRequired()])
    #query_img_urls=StringField("Query Images",validators=[DataRequired()])