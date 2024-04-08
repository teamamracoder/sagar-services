from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,SelectField
from wtforms.validators import DataRequired


class CreateServiceQnAForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    service_id = SelectField("Service", validators=[DataRequired()])
    answer = TextAreaField("Answer")
    user_id = IntegerField("User Id", validators=[DataRequired()])

class UpdateServiceQnAForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    service_id = SelectField("Service", validators=[DataRequired()])
    answer = TextAreaField("Answer")
    user_id = IntegerField("User Id", validators=[DataRequired()])
