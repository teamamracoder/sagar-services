from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class CreateProductQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])


class UpdateProductQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
