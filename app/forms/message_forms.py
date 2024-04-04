from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, TextAreaField, FieldList
from wtforms.validators import DataRequired, URL

class CreateMessageForm(FlaskForm):
    conversation_id = IntegerField("Conversation Id", validators=[DataRequired()])
    message_text=StringField("Message text",validators=[DataRequired()])
    created_by = IntegerField("Created By (Integer field)", validators=[DataRequired()])


class UpdateMessageForm(FlaskForm):
    conversation_id = IntegerField("Conversation Id", validators=[DataRequired()])
    message_text=StringField("Message text",validators=[DataRequired()])
    created_by = IntegerField("Created By (Integer field)", validators=[DataRequired()])