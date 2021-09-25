from flask import render_template, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from flask_login.utils import login_required
from werkzeug.utils import redirect

from app.models import Hospital
from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        hospital = Hospital.query.filter_by(email=form.email.data).first()
        if hospital is not None and hospital.verify_password(form.password.data):
            login_user(hospital,form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
                session['name'] = hospital.name
            return redirect(next)
        else:
            flash("Invalid Username / Password")
    return render_template('auth/login.html',form=form),200

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    session['name'] = "Normal User"
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hospital = Hospital(name=form.name.data,
        email=form.email.data,
        pincode=form.pincode.data,
        password=form.password.data)
        db.session.add(hospital)
        db.session.commit()

        flash("You can now login !")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)