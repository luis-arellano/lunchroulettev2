from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# db_uri = os.environ.get('DATABASE_URI')
uri = 'mysql+mysqlconnector://root:rockclimber1!@database-1.ciiowaujelgi.us-west-2.rds.amazonaws.com:3306/lunchroulette'

app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)

# How to connect to the database from terminal.
# mysql -h <host endpoint. -P 3306 -u root -p
