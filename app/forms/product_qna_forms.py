from flask_wtf import FlaskForm
from wtforms import IntegerField,TextAreaField,SelectField
from wtforms.validators import DataRequired


class CreateProductQnAForm(FlaskForm):
    product_id = IntegerField("Product id", validators=[DataRequired()])
    question = TextAreaField("Question", validators=[DataRequired()])

class UpdateProductQnAForm(FlaskForm):
    product_id = SelectField("Product", validators=[DataRequired()])
    question = TextAreaField("Question", validators=[DataRequired()])
    answer = TextAreaField("Answer")
    