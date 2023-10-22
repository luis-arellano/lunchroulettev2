from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import logging
from flask_migrate import Migrate

# Load environment variables from .env file
load_dotenv('.env')

#The static_url_path, static_folder, and template_folder are configured 
#to serve static files and templates from the frontend/build directory. 
#This is so that the React frontend is built into this directory.

app = Flask(__name__, static_url_path='',
            static_folder='frontend/build/static', template_folder='frontend/build')
app.logger.setLevel(logging.INFO)
db_uri = os.environ.get('LUNCHROULETTE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

# How to connect to the database from terminal.
# mysql -h <host endpoint. -P 3306 -u root -p

# Link the migration tool to the app and the database
migrate = Migrate(app, db)
