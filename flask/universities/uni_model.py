from setup import db


class University(db.Model):
    __tablename__ = 'Universities'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(255))
    shortName = db.Column(db.String(45))
    creationDate = db.Column(db.Date)