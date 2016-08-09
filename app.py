import sys
import re

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from module.forms import SignUpForm

import database
from module import init 
from module import models

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)
db.create_all()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def sign_up():
    flash('All fields are required')
    form = SignUpForm()
    return render_template('sign_up.html', form=form)

@app.route('/signin')
def sign_in():
    return 'sign in' 

@app.route('/dashboard')
def dashboard():
    return init.test_print()

# error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    database.init_db()
    # user = models.User('chann@chann.kr', 'asdf', 'CHANN', '01012341234', 1)
    # database.db_session.add(user)
    # database.db_session.commit()
    app.run(port=8000, threaded=True, debug=True)

