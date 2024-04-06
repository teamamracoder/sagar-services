from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField
from wtforms.validators import DataRequired


class CreateProductQuestionForm(FlaskForm):
    product_id = IntegerField("Service Id", validators=[DataRequired()])
    question = TextAreaField("Question", validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired()])

class UpdateProductQuestionForm(FlaskForm):
    product_id = IntegerField("Service Id", validators=[DataRequired()])
    question = TextAreaField("Question", validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired()])