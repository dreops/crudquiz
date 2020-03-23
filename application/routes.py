from flask import render_template
from application import app
from forms import QuestionForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/add')
def add():
    return render_template('add.html', title='Add Questions')

@app.route('/answers')
def answers():
    return render_template('answers.html', title='Answers')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title='The Quiz')

@app.route('/create', methods=['GET','POST'])
def create():
    form = QuestionForm()
    return render_template('create.html', title='Create Question', form = form)