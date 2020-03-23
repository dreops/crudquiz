from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QuestionForm(FlaskForm):
    quizquestion = StringField('Question')
    