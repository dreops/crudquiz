from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    quizquestion = StringField('Question', validators=[DataRequired()])
    