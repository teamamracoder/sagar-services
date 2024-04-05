from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

class CreateProductReviewForm(FlaskForm):
    product_id = IntegerField('Product', validators=[DataRequired()])
    user_id = IntegerField('User id', validators=[DataRequired()])
    review_title=StringField('Title', validators=[DataRequired()])
    description=TextAreaField('Description', validators=[DataRequired()])
    rating=FloatField('Rating', validators=[DataRequired()])

class UpdateProductReviewForm(FlaskForm):
    product_id = SelectField('Product', validators=[DataRequired()])
    user_id = IntegerField('User id', validators=[DataRequired()])
    review_title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
