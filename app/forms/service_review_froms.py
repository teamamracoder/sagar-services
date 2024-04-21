from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class CreateServiceReviewForm(FlaskForm):
    service_id = IntegerField('Service', validators=[DataRequired()])
    review_title=StringField('Title', validators=[DataRequired()])
    description=TextAreaField('Description', validators=[DataRequired()])
    rating=FloatField('Rating', validators=[DataRequired()])
    service_review_img_urls = MultipleFileField("Images")
