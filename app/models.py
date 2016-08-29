# models.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from app import app

### SQLAlchemy Data Type
### Integer: an integer
### String (size): a string with a maximum length
### Text: some longer unicode text
### DateTime: date and time expressed as Python datetime object.mroFloatstores floating point values
### Boolean: stores a boolean value
### PickleType: stores a pickled Python object
### LargeBinary: stores large arbitrary binary data

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(20))
    phone = db.Column(db.String(30))
    is_admin = db.Column(db.Integer)
    monitor = db.relationship('Monitor', backref='monitor', lazy='dynamic')
    alertlog = db.relationship('AlertLog', backref='alertlog', lazy='dynamic')

    def __init__(self, email_id, password, name, phone, is_admin=0):
        self.email_id = email_id
        self.password = password
        self.name = name
        self.phone = phone
        self.is_admin = is_admin

    # __repr__ method tells Python how to print objects of this class. We will use this for debugging.
    def __repr__(self):
        return '<User %r>' % (self.email_id)

class Monitor(db.Model):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Boolean)
    label = db.Column(db.String(20))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    monitor_log = db.relationship('MonitorLog', backref='monitor_log', lazy='dynamic')
    alert_log = db.relationship('AlertLog', backref='alert_log', lazy='dynamic')

class MonitorLog(db.Model):
    __tablename__ = 'monitor_log'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id'))

class AlertLog(db.Model):
    __tablename__ = 'alert_log'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id'))
