from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class CreateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    first_name=StringField("First Name",validators=[DataRequired()])
    last_name=StringField("Last Name",validators=[DataRequired()])
    mobile=StringField("Mobile",validators=[DataRequired()])


class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    first_name=StringField("First Name",validators=[DataRequired()])
    last_name=StringField("Last Name",validators=[DataRequired()])
    mobile=StringField("Mobile",validators=[DataRequired()])