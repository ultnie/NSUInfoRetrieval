from datetime import date

from flask import render_template, redirect, Blueprint
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

from setup import db
from universities.uni_model import University

university_blueprint = Blueprint('university_blueprint', __name__, template_folder='templates', static_folder='static')


@university_blueprint.route('/')
def university_list():
    unis = University.query.all()
    return render_template('uni_list.html', universities=unis)


@university_blueprint.route('/<uni_id>')
def uni(uni_id):
    uni = db.session.query(University).get(uni_id)
    return render_template('uni.html', id=uni.id, fullName=uni.fullName, shortName=uni.shortName, creationDate=uni.creationDate)


class CreateForm(FlaskForm):
    fullName = StringField("Full Name: ", validators=[DataRequired(), Length(max=255)])
    shortName = StringField("Short Name: ", validators=[DataRequired(), Length(max=45)])
    creationDate = DateField("Creation Date: ")
    create = SubmitField("Create")


@university_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_university():
    form = CreateForm()
    if form.validate_on_submit():
        uni = University(fullName=form.fullName.data, shortName=form.shortName.data, creationDate=date(form.creationDate.data.year, form.creationDate.data.month, form.creationDate.data.day))
        db.session.add(uni)
        db.session.commit()
        return redirect('/university')
    return render_template("create_uni.html", form=form)


@university_blueprint.route('/<uni_id>/update', methods=['GET', 'POST'])
@login_required
def update_university(uni_id):
    form = CreateForm()
    form.create.label.text = "Update"
    if form.validate_on_submit():
        db.session.query(University).filter(University.id == uni_id).update({'fullName': form.fullName.data, 'shortName': form.shortName.data, 'creationDate': date(form.creationDate.data.year, form.creationDate.data.month, form.creationDate.data.day)})
        db.session.commit()
        return redirect('/university')
    return render_template("update_uni.html", form=form)


@university_blueprint.route('/<uni_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_university(uni_id):
    db.session.query(University).filter(University.id == uni_id).delete()
    db.session.commit()
    return redirect('/university')