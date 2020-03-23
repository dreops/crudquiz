from application import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizquestions = db.Column(db.String(255), unique=True)
    answer_id = db.relationship('Answers', backref='', lazy=True)

    def __repr_(self):
        return f"Questions('{self.quizquestions}')"

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_answers = db.Column(db.Integer, unique=True)
    correct_answer = db.Column(db.Integer, nullable=False)

    def __repr_(self):
        return f"Answers('{self.users_answers}')"