from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateCategoryForm(FlaskForm):
    category_name = StringField("category_name", validators=[DataRequired()])
    category_img_url = StringField("category_img_url")

class UpdateCategoryForm(FlaskForm):
    category_name = StringField("category_name", validators=[DataRequired()])
    category_img_url = StringField("category_img_url")