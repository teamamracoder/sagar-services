from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, TextAreaField, FieldList
from wtforms.validators import DataRequired, URL

class CreateConversationForm(FlaskForm):
    user_id = IntegerField("user", validators=[DataRequired()])
    staff_id = IntegerField("staff", validators=[DataRequired()])


class UpdateConversationForm(FlaskForm):
    user_id = IntegerField("user", validators=[DataRequired()])
    staff_id = IntegerField("staff", validators=[DataRequired()])