from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='',
            static_folder='frontend/build/static', template_folder='frontend/build')
db_uri = os.environ.get('LUNCHROULETTE_URI')

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# How to connect to the database from terminal.
# mysql -h <host endpoint. -P 3306 -u root -p
