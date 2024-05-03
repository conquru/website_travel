from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    city_start = StringField('city start', validators=[DataRequired()])
    city_end = IntegerField('city end', validators=[DataRequired()])
    time = IntegerField('time', validators=[DataRequired()])
