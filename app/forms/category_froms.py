from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateCategoryForm(FlaskForm):
    category = StringField("Category", validators=[DataRequired()])