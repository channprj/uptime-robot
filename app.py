#!flask/bin/python
from flask import Flask
import test

app = Flask(__name__)

@app.route('/')
def index():
    return test.test_print()

if __name__ == '__main__':
    app.run(port=8000, debug=True)
