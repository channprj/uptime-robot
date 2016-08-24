# views.py
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import flash
from flask import redirect
from flask import request
from flask import g
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
@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.now()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()

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
    #print(request.form['email_id'])
    if form.validate_on_submit():
        flash('Hello, %s, Wait seconds... ' % form.name)
        g.user.email_id = form.email_id
        g.user.password = form.password
        g.user.name = form.name
        g.user.phone = form.phone
        db.session.add(g.user)
        db.session.commit()
        flash(gettext('User has been saved.'))
        return redirect('/dashboard')
#    elif request.method != 'POST':
#        form.email_id = g.user.email_id
#        form.name = g.user.name
#        form.phone = g.user.phone
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/signin')
def signin():
    return 'sign in'
