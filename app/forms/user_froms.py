from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, DateField, RadioField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed


class CreateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    first_name=StringField("First Name",validators=[DataRequired()])
    last_name=StringField("Last Name",validators=[DataRequired()])
    mobile=StringField("Mobile",validators=[DataRequired()])
    profile_photo_url = FileField("Profile Picture",validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])

class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    first_name=StringField("First Name",validators=[DataRequired()])
    last_name=StringField("Last Name",validators=[DataRequired()])
    mobile=StringField("Mobile",validators=[DataRequired()])
    address = TextAreaField("Address",validators=[DataRequired()])
    dob = DateField("DOB",validators=[DataRequired()])
    gender = RadioField("Gender", choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')],validators=[DataRequired()])
    profile_photo_url = FileField("Profile Picture")