from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

class CreateServiceReviewForm(FlaskForm):
    service_id = SelectField('Service', validators=[DataRequired()])
    review_title=StringField('Title', validators=[DataRequired()])
    description=TextAreaField('Description', validators=[DataRequired()])
    rating=FloatField('Rating', validators=[DataRequired()])

class UpdateServiceReviewForm(FlaskForm):
    service_id = SelectField('Service', validators=[DataRequired()])
    review_title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
