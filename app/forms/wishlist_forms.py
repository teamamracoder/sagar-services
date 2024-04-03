from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CreateWishlistForm(FlaskForm):
    product_id = IntegerField("Product Id", validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired()])

