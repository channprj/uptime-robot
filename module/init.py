# init.py
import __future__
import sys
import httplib
import urllib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
db = SQLAlchemy(app)

### SQLAlchemy Data Type
### Integer: an integer
### String (size): a string with a maximum length
### Text: some longer unicode text
### DateTime: date and time expressed as Python datetime object.mroFloatstores floating point values
### Boolean: stores a boolean value
### PickleType: stores a pickled Python object
### LargeBinary: stores large arbitrary binary data

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(20))
    phone = db.Column(db.String(30))
    is_admin = db.Column(db.Integer)
    monitor = db.relationship('Monitor', backref='monitor', lazy='dynamic')

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Boolean)
    label = db.Column(db.String(20))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    monitor_log = db.relationship('MonitorLog', backref='monitor_log', lazy='dynamic')

class MonitorLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id'))

class HTTPChecker(object):
    """docstring for HTTPChecker"""
    def __init__(self, arg):
        super(HTTPChecker, self).__init__()
        self.arg = arg

def test_print():
    res = send_http_request('chann.kr')
    return str(res)

def send_http_request(url):
    conn = httplib.HTTPConnection(url)
    conn.request('HEAD', '')
    res = conn.getresponse()
    status = res.status
    # status = res.getheaders()
    return status, res.getheaders()

def send_ping_request():
    pass

def alert_email():
    pass

def alert_sms():
    pass

def set_interval():
    pass

def __init__():
    return
