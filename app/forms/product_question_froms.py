from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

class CreateProductQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])

    # category_img_url = FileField("Image",validators=[FileRequired()])
    # category_img_url = StringField("Image")


class UpdateProductQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    # category_img_url = FileField("Image")
    # category_img_url = StringField("Image")