from application import db

class Questions(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    quizquestions = db.Column(db.String(255), unique=True)
    answer_id = db.Column(db.Integer(), db.ForeignKey("Answers.id"))

    def __repr_(self):
        return f"Questions('{self.quizquestions}')"

class Answers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
#    users_answers = db.Column(db.Integer() )
    correct_answer = db.Column(db.Integer(), nullable=False)
    ans = db.relationship("Questions", backref = "answer")

    def __repr_(self):
        return f"Answers('{self.users_answers}')"