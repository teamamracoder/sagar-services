from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired

class CreateProductQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = IntegerField('Product',  validators=[DataRequired()])


class UpdateProductQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', validators=[DataRequired()])
