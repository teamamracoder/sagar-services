from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, TextAreaField, FieldList
from wtforms.validators import DataRequired, URL

class CreateProductForm(FlaskForm):
    category_id = IntegerField("category_id", validators=[DataRequired()])
    product_name = StringField("product_name", validators=[DataRequired()])
    brand = StringField("brand", validators=[DataRequired()])
    model = StringField("model", validators=[DataRequired()])
    price = FloatField("price", validators=[DataRequired()])
    discount = FloatField("discount")
    stock = IntegerField("stock", validators=[DataRequired()])
    product_img_urls = FieldList(StringField("product_img_urls", validators=[URL()]))
    specifications = TextAreaField("specifications", validators=[DataRequired()])
    payment_methods = FieldList(IntegerField("payment_methods", validators=[DataRequired()]))
    available_area_pincodes = FieldList(StringField("available_area_pincodes", validators=[DataRequired()]))
    return_policy = TextAreaField("return_policy", validators=[DataRequired()])


class UpdateProductForm(FlaskForm):
    category_id = IntegerField("category_id", validators=[DataRequired()])
    product_name = StringField("product_name", validators=[DataRequired()])
    brand = StringField("brand", validators=[DataRequired()])
    model = StringField("model", validators=[DataRequired()])
    price = FloatField("price", validators=[DataRequired()])
    discount = FloatField("discount")
    stock = IntegerField("stock", validators=[DataRequired()])
    product_img_urls = FieldList(StringField("product_img_urls", validators=[URL()]))
    specifications = TextAreaField("specifications", validators=[DataRequired()])
    payment_methods = FieldList(IntegerField("payment_methods", validators=[DataRequired()]))
    available_area_pincodes = FieldList(StringField("available_area_pincodes", validators=[DataRequired()]))
    return_policy = TextAreaField("return_policy", validators=[DataRequired()])