import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Secure: Generate a random secret key
CSRF_ENABLED = True
SECRET_KEY = 'conceal-it'
#SECRET_KEY = os.urandom(24)

# SQLAlchemy database configuration
if os.environ.get('DB_URI') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/test.db' % (os.path.dirname(__file__))
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URI']
SQLALCHEMY_RECORD_QUERIES = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'migrates')
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Debugging
DEBUG = True

# Admin list
ADMINS = ['chann@chann.kr',]
