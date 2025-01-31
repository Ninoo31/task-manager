from app.config import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), default="pending")
    priority = db.Column(db.String(20), default="low")
    deadline = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Task {self.title}>"
