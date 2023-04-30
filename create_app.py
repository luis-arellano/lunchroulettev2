from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='',
            static_folder='../frontend/build', template_folder='../frontend/build')
db_uri = os.environ.get('LUNCHROULETTE_URI')

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

# How to connect to the database from terminal.
# mysql -h <host endpoint. -P 3306 -u root -p
