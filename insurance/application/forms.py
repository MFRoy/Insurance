from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class CarForm(FlaskForm):
    description = StringField("Add a Vehicle")
    owner = SelectField("Select Owner", choices=[])
    submit = SubmitField("Submit")

class OwnerForm(FlaskForm):
    name = StringField("Add a New Owner")
    submit = SubmitField("Submit")


# class CoverForm(FlaskForm):
#     description = StringField("Add a Policy")
#     submit = SubmitField("Submit")