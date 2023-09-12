from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#The static_url_path, static_folder, and template_folder are configured 
#to serve static files and templates from the frontend/build directory. 
#This is so that the React frontend is built into this directory.

app = Flask(__name__, static_url_path='',
            static_folder='frontend/build/static', template_folder='frontend/build')
db_uri = os.environ.get('LUNCHROULETTE_URI')

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

# How to connect to the database from terminal.
# mysql -h <host endpoint. -P 3306 -u root -p
