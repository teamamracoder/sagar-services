from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, TextAreaField
from wtforms.validators import DataRequired

class CreateProductReviewForm(FlaskForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    review_title=StringField('Title', validators=[DataRequired()])
    description=TextAreaField('Description', validators=[DataRequired()])
    rating=FloatField('Rating', validators=[DataRequired()])

class UpdateProductReviewForm(FlaskForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    review_title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
