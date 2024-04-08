from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired

class CreateStaffForm(FlaskForm):
    salary = FloatField("Salary", validators=[DataRequired()])
    qualification = StringField("Qualification", validators=[DataRequired()])
    join_date = DateField("Join Date", validators=[DataRequired()])
    leave_date = DateField("Leave Date", validators=[DataRequired(False)])
    department = SelectField("Department", validators=[DataRequired()], coerce=int)


class UpdateStaffForm(FlaskForm):
    salary = FloatField("Salary", validators=[DataRequired()])
    qualification = StringField("Qualification", validators=[DataRequired()])
    join_date = DateField("Join Date", validators=[DataRequired()])
    leave_date = DateField("Leave Date", validators=[DataRequired(False)])
    department = SelectField("Department", validators=[DataRequired()], coerce=int)