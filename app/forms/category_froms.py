from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = StringField("Image")


class UpdateCategoryForm(FlaskForm):
    category_name = StringField("Name", validators=[DataRequired()])
    category_img_url = StringField("Image")