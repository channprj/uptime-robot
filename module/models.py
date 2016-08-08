# models.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import Base

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

class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(20))
    phone = db.Column(db.String(30))
    is_admin = db.Column(db.Integer)
    monitor = db.relationship('Monitor', backref='monitor', lazy='dynamic')
    alertlog = db.relationship('AlertLog', backref='alertlog', lazy='dynamic')

    def __init__(self, name=None, email_id=None, password=None, phone=None, is_admin=None):
        self.name = name
        self.email_id = email_id
        self.password = password
        self.phone = phone
        self.is_admin = is_admin

class Monitor(Base):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Boolean)
    label = db.Column(db.String(20))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    monitor_log = db.relationship('MonitorLog', backref='monitor_log', lazy='dynamic')
    alert_log = db.relationship('AlertLog', backref='alert_log', lazy='dynamic')

class MonitorLog(Base):
    __tablename__ = 'monitor_log'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id'))

class AlertLog(Base):
    __tablename__ = 'alert_log'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id'))
