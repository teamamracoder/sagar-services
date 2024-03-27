from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired


class StringArrayField(StringField):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [value.strip() for value in valuelist[0].split(',')]
        else:
            self.data = []
class IntegerArrayField(IntegerField):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [value.strip() for value in valuelist[0].split(',')]
        else:
            self.data = []

class CreateProductForm(FlaskForm):
    product_name = StringField("Product Name", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    discount = FloatField("Discount", validators=[DataRequired()])
    stock = IntegerField("Stock", validators=[DataRequired()])
    specifications = TextAreaField("Specifications", validators=[DataRequired()])
    category_id = IntegerField("Category", validators=[DataRequired()])
    available_area_pincodes = IntegerArrayField("Available Area Pincode", validators=[DataRequired()])
    payment_methods = IntegerArrayField("Payment Methods", validators=[DataRequired()])
    product_img_urls = StringArrayField("Product img urls")
    return_policy = StringField("Return Policy", validators=[DataRequired()])



   