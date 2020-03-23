from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntergerField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    quizquestion = StringField('Question', validators=[DataRequired()])
    