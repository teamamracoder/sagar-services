from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class CreateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'webp','gif'])])


class UpdateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = FileField('Image (selecting an Image will replace previous One)')