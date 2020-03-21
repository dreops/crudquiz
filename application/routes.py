from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')

@app.route('/add')
def add():
    return render_template('add.html', title='Add Questions')

@app.route('/answers')
def add():
    return render_template('answers.html', title='Answers')

@app.route('/quiz')
def add():
    return render_template('quiz.html', title='The Quiz')
