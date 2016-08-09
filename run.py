#!flask/bin/python
from app import app
app.run(port=8000, threaded=True, debug=True)
