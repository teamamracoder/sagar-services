from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField
from wtforms.validators import DataRequired


class CreateServiceAnswerForm(FlaskForm):
    created_by = IntegerField("Created_by Id", validators=[DataRequired()])
    question_id = IntegerField("Question Id", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])
    staff_id = IntegerField("Staff Id", validators=[DataRequired()])

class UpdateServiceAnswerForm(FlaskForm):
    created_by = IntegerField("Created_by Id", validators=[DataRequired()])
    question_id = IntegerField("Question Id", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])
    staff_id = IntegerField("Staff Id", validators=[DataRequired()])