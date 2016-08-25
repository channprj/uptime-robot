# views.py
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import flash
from flask import redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from app import app
from app import db
from app import lm
from app import init
from .forms import SignUpForm
from .models import User
from .models import Monitor
from .models import MonitorLog
from .models import AlertLog

# init
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return init.test_print()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(form.email_id.data, form.password.data, form.name.data, form.phone.data)
        db_session.add(user)
        flash('Hello, %s, Wait seconds... ' % form.name)
        flash('User has been saved.')
        
        return redirect('/dashboard')
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/signin')
def signin():
    return 'sign in'
