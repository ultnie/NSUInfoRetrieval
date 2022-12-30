from setup import db


class Student(db.Model):
    __tablename__ = 'Students'
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(45))
    firstName = db.Column(db.String(45))
    patronymic = db.Column(db.String(45))
    birthDate = db.Column(db.Date)
    university = db.Column(db.ForeignKey("Universities.id"))
    year = db.Column(db.Integer)