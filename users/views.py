from flask import render_template, request, session, url_for, redirect, flash, Blueprint

users_blueprint = Blueprint('users', __name__, template_folder = 'templates')

from core import app, db, bcrypt
from sqlalchemy.exc import IntegrityError
from forms import SignupForm, LoginForm
from models import User
from flask.ext.login import login_user, login_required, current_user, logout_user

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    result_message = None
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user = User(first_name = form.first_name.data, last_name = form.last_name.data,
                email = form.user_email.data, title = form.title.data, password = form.password.data)
                db.session.add(user)
                db.session.commit()
                result_message = str(form.first_name.data) + " successfully registered."
            except Exception as e:
                result_message = e
                db.session.rollback()
        else:
            result_message = 'Ensure your passwords match and you entered a valid email address.'
            return render_template('signup.html', result_message=result_message, form=form)
        return render_template('signup.html', result_message=result_message, form=form)
    return render_template('signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email = form.login_email.data).first()
            if user is not None and bcrypt.check_password_hash(user.password, form.login_password.data):
                flash('You were logged in.')
                login_user(user)
                return redirect(url_for('assets.viewassets'))
            else:
                flash('Incorrect username or password.')
    return render_template('login.html', form=form)


@login_required 
@users_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('users.login'))
    
