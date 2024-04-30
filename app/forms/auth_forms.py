from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email_or_mobile = StringField("Email/Phone No.", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class VerifyOtpForm(FlaskForm):
    otp = PasswordField("OTP", validators=[DataRequired()])
