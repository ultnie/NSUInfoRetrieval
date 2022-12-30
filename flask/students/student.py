from datetime import date

from flask import render_template, Blueprint, redirect
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

from setup import db, app
from students.student_model import Student
from universities.uni_model import University

student_blueprint = Blueprint('student_blueprint', __name__, template_folder='templates', static_folder='static')


@student_blueprint.route('/')
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students=students)


@student_blueprint.route('/<student_id>')
def student(student_id):
    student = db.session.query(Student).get(student_id)
    return render_template('student.html', id=student_id, lastName=student.lastName, firstName=student.firstName, patronymic=student.patronymic, birthDate=student.birthDate, university=student.university, year=student.year)


class CreateForm(FlaskForm):
    lastName = StringField("Last Name: ", validators=[DataRequired(), Length(max=45)])
    firstName = StringField("First Name: ", validators=[DataRequired(), Length(max=45)])
    patronymic = StringField("Patronymic: ", validators=[DataRequired(), Length(max=45)])
    birthDate = DateField("Birth Date: ")
    with app.app_context():
        university = SelectField("University: ", choices=db.session.query(University.id).all())
    year = IntegerField("Year: ")
    create = SubmitField("Create")


@student_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_student():
    form = CreateForm()
    if form.validate_on_submit():
        stud = Student(lastName=form.lastName.data, firstName=form.firstName.data, patronymic=form.patronymic.data, birthDate=date(form.birthDate.data.year, form.birthDate.data.month, form.birthDate.data.day), university=int(form.university.data.strip('(),')), year=form.year.data)
        db.session.add(stud)
        db.session.commit()
        return redirect('/student')
    return render_template('create_student.html', form=form)


@student_blueprint.route('/<student_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_student(student_id):
    db.session.query(Student).filter(Student.id == student_id).delete()
    db.session.commit()
    return redirect('/student')


@student_blueprint.route('/<student_id>/update', methods=['GET', 'POST'])
@login_required
def update_student(student_id):
    form = CreateForm()
    form.create.label.text = "Update"
    if form.validate_on_submit():
        db.session.query(Student).filter(Student.id == student_id).update({'lastName': form.lastName.data, 'firstName': form.firstName.data, 'patronymic': form.patronymic.data,'birthDate': date(form.birthDate.data.year, form.birthDate.data.month, form.birthDate.data.day),'university': int(form.university.data.strip('(),')), 'year': form.year.data})
        db.session.commit()
        return redirect('/student')
    return render_template('update_student.html', form=form)
