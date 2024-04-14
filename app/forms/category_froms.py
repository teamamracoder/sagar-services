from flask_wtf import FlaskForm
from wtforms import StringField, FileField, MultipleFileField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = MultipleFileField('Images', validators=[DataRequired()])


class UpdateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = MultipleFileField('Images', validators=[DataRequired()])