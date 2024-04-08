from flask_wtf import FlaskForm
from wtforms import IntegerField,TextAreaField
from wtforms.validators import DataRequired


class CreateProductAnswerForm(FlaskForm):
    question_id = IntegerField("Question Id", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])

class UpdateProductAnswerForm(FlaskForm):
    question_id = IntegerField("Question Id", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])