from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,SelectField
from wtforms.validators import DataRequired


class CreateServiceQnAForm(FlaskForm):
    service_id = IntegerField("Services", validators=[DataRequired()])
    question = TextAreaField("Question", validators=[DataRequired()])

class UpdateServiceQnAForm(FlaskForm):
    service_id = IntegerField("Services", validators=[DataRequired()])
    question = StringField("Question", validators=[DataRequired()])
    answer = TextAreaField("Answer")
    