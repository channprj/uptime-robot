import sys
from module import test
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return test.test_print()

if __name__ == '__main__':
    app.run(port=8000, debug=True)
