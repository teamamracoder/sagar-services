from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class CreateRoleForm(FlaskForm):
    user_id = IntegerField("User Id", validators=[DataRequired()])
    role = IntegerField("Role", validators=[DataRequired()])
