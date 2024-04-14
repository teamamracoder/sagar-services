from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, FieldList, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class CreateProductForm(FlaskForm):
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    product_name = StringField("product_name", validators=[DataRequired()])
    brand = StringField("brand", validators=[DataRequired()])
    model = StringField("model", validators=[DataRequired()])
    price = FloatField("price", validators=[DataRequired()])
    discount = FloatField("discount")
    stock = IntegerField("stock", validators=[DataRequired()])
    product_img_urls = FieldList(StringField("product_img_urls"))
    specifications = TextAreaField("specifications", validators=[DataRequired()])
    payment_methods = SelectMultipleField("payment_methods (hold ctrl and select)", validators=[DataRequired()], coerce=int)
    available_area_pincodes = StringField("Available Area Pincode (use comma separated)", validators=[DataRequired()])
    return_policy = TextAreaField("return_policy", validators=[DataRequired()])
    # category_img_url = MultipleFileField('Images', validators=[DataRequired()])

class UpdateProductForm(FlaskForm):
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    product_name = StringField("product_name", validators=[DataRequired()])
    brand = StringField("brand", validators=[DataRequired()])
    model = StringField("model", validators=[DataRequired()])
    price = FloatField("price", validators=[DataRequired()])
    discount = FloatField("discount")
    stock = IntegerField("stock", validators=[DataRequired()])
    product_img_urls = FieldList(StringField("product_img_urls"))
    specifications = TextAreaField("specifications", validators=[DataRequired()])
    payment_methods = SelectMultipleField("payment_methods (hold ctrl and select)", validators=[DataRequired()], coerce=int)
    available_area_pincodes = StringField("Available Area Pincode (use comma separated)", validators=[DataRequired()])
    return_policy = TextAreaField("return_policy", validators=[DataRequired()])
    # category_img_url = MultipleFileField('Images', validators=[DataRequired()])