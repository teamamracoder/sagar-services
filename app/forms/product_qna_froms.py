from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CreateProductQnAForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = IntegerField('Product', validators=[DataRequired()])
    answer = StringField("Answer", validators=[DataRequired()])
