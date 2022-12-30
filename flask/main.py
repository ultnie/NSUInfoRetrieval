from flask import render_template, redirect, url_for, request, flash
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from setup import app, db, login_manager, auth
from students.student import student_blueprint
from universities.university import university_blueprint
from user_model import User

app.register_blueprint(university_blueprint, url_prefix='/university')
app.register_blueprint(student_blueprint, url_prefix='/student')


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

#from universities.uni_model import University
#from students.student_model import Student
#from user_model import User

#with app.app_context():
#    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    print(user.email, user.password)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    next_page = request.form.get('next')
    print(User.query.filter_by(email=email).first().get_id())
    login_user(load_user(User.query.filter_by(email=email).first().get_id()))
    if next_page:
        return redirect(next_page)
    return redirect(url_for("index"))


@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


app.register_blueprint(auth)


if __name__ == "__main__":
    app.run()
