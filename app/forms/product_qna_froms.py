from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from .product_question_froms import CreateProductQuestionForm, UpdateProductQuestionForm
from .product_answer_froms import CreateProductAnswerForm, UpdateProductAnswerForm

class CreateProductQnAForm(CreateProductQuestionForm,CreateProductAnswerForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])

class UpdateProductQnAForm(UpdateProductQuestionForm,UpdateProductAnswerForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])