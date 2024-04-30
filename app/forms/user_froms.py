from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, TextAreaField, DateField, RadioField, EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed


class CreateUserForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    first_name=StringField("First Name",validators=[DataRequired()])
    last_name=StringField("Last Name",validators=[DataRequired()])
    mobile=StringField("Mobile",validators=[DataRequired()])
    profile_photo_url = FileField("Profile Picture",validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    street = StringField("Street Address")
    landmark = StringField("Landmark")
    address_line = StringField("Address Line")
    city = StringField("City")
    state = StringField("State")
    pincode=IntegerField("Pincode")

class UpdateUserForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    first_name=StringField("First Name",validators=[DataRequired()])
    last_name=StringField("Last Name",validators=[DataRequired()])
    mobile=StringField("Mobile",validators=[DataRequired()])
    profile_photo_url = FileField("Adding an Image will replace the previous one",validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    street = StringField("Street Address")
    landmark = StringField("Landmark")
    address_line = StringField("Address Line")
    city = StringField("City")
    state = StringField("State")
    pincode=IntegerField("Pincode")
    dob = DateField("DOB")
    gender = RadioField("Gender", choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])