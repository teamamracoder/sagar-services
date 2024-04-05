from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired

class CreateProductQnAForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = IntegerField('Product', validators=[DataRequired()])
    answer = StringField("Answer")
    user_id = IntegerField("user id", validators=[DataRequired()])

class UpdateProductQnAForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    answer = StringField("Answer")
    user_id = IntegerField("user id", validators=[DataRequired()])
