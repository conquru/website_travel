from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    city_start = StringField('Ваш город ', validators=[DataRequired()])
    city_end = StringField('Город назначения', validators=[DataRequired()])
    time = StringField('Дата', validators=[DataRequired()])
    submit = SubmitField('Найти')