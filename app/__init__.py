__author__ = "CHANN"
__email__ = "chann@chann.kr"
__version__ = "0.0.0"

import os
import sys
import re

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import url_for
from flask import redirect
from flask import request
from flask import flash
from flask_sqlalchemy import SQLAlchemy

from app.forms import SignUpForm
from app import init

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'signin'

from app import models
from app import views
