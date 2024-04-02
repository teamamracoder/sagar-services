from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

class CreateProductAnswerForm(FlaskForm):
    answer = StringField("Answer", validators=[DataRequired()])
    # category_img_url = FileField("Image",validators=[FileRequired()])
    # category_img_url = StringField("Image")


class UpdateProductAnswerForm(FlaskForm):
    answer = StringField("Answer", validators=[DataRequired()])
    # category_img_url = FileField("Image")
    # category_img_url = StringField("Image")