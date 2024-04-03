from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from .product_question_froms import CreateProductQuestionForm, UpdateProductQuestionForm

class CreateProductQnAForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    answer = StringField("Answer", validators=[DataRequired()])
