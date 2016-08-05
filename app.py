import sys
from module import init 
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def sign_up():
    return init.test_print()

@app.route('/signin')
def sign_in():
    return init.test_print()

@app.route('/dashboard')
def dashboard():
    return init.test_print()

# error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=8000, threaded=True, debug=True)
