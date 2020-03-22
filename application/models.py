from application import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizquestions = db.Column(db.String(255), unique=True)
    answer_id = db.Column(db.Integer)

    def __repr_(self):
        return f"Questions('{self.quizquestions}')"

# h = Questions()
# print(h)
