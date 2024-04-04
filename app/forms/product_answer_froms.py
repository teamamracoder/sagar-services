from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class CreateProductAnswerForm(FlaskForm):
    answer = StringField("Answer", validators=[DataRequired()])
    question_id = SelectField('Question', coerce=int, validators=[DataRequired()])


class UpdateProductAnswerForm(FlaskForm):
    answer = StringField("Answer", validators=[DataRequired()])
    question_id = SelectField('Question', coerce=int, validators=[DataRequired()])