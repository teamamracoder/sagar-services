from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField
from wtforms.validators import DataRequired


class CreateServiceQuestionForm(FlaskForm):
    created_by = IntegerField("created_by Id", validators=[DataRequired()])
    service_id = IntegerField("service Id", validators=[DataRequired()])
    question = TextAreaField("Question", validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired()])