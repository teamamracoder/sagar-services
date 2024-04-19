from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, IntegerField, SelectField, MultipleFileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class CreateProductReviewForm(FlaskForm):
    product_id = IntegerField('Product Id', validators=[DataRequired()])
    review_title=StringField('Title', validators=[DataRequired()])
    description=TextAreaField('Description', validators=[DataRequired()])
    rating=FloatField('Rating', validators=[DataRequired()])
    product_review_img_urls=MultipleFileField("Images",validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif'])])    

class UpdateProductReviewForm(FlaskForm):
    product_id = SelectField('Product Id', validators=[DataRequired()])
    review_title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    product_review_img_urls=MultipleFileField("Images")