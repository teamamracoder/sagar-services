from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = FileField('Image')


class UpdateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = FileField('Image (selecting an Image will replace previous One)')