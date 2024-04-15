from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CreateConversationForm(FlaskForm):
    user_id=IntegerField("User id",validators=[DataRequired()])

    