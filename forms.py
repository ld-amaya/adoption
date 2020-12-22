from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class PetForms(FlaskForm):
    """Define forms to be used in Pet Adoption"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"),
                 ("dog", "Dog"),
                 ("rabbit", "Rabbit")])

    photo = StringField(
        "Photo URL",
        validators=[Optional(), URL()])

    age = IntegerField(
        "Age",
        validators=[Optional(),
                    NumberRange(min=0, max=25)])

    notes = TextAreaField("Comments / Notes",
                          validators=[Optional()])


class EditPetForm(FlaskForm):

    photo = StringField(
        "Photo URL",
        validators=[Optional(), URL()])

    notes = TextAreaField("Comments / Notes",
                          validators=[Optional()])

    available = BooleanField("Available",
                             validators=[Optional()])
