from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CreateCartForm(FlaskForm):
    product_id = IntegerField("Product Id", validators=[DataRequired()])

