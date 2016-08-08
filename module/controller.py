# controller.py
from flask import render_template
from models import User
from models import Monitor
from models import MonitorLog
from models import AlertLog

@app.route('/dashboard/<id>')
def view_monitor_list(id):
    list = Monitor.query.all(id)
    if list == None:
        return abort(404)
    return render_template('monitor_list.html', list=list)
