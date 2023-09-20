import os
from flask import Flask, request, jsonify, session, redirect, send_from_directory, make_response, render_template
from flask import Response
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from models import User, Match, Review
from create_app import app, db
from flask_cors import CORS  # comment this on deployment
import json
import matches

# Initialize the database
db.init_app(app)

if os.environ.get('IS_DEV') == 'true':
    app.logger.info('******** DEV Environment***** ')
    CORS(app, origins="http://localhost:3000", supports_credentials=True)
else:
    app.logger.info('******** PROD Environment***** ')

CORS(app, origins="http://localhost:3000", supports_credentials=True)

app.config['SECRET_KEY'] = '36&462134kjKDhuIS_d23'
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=False,
    SESSION_COOKIE_SAMESITE=None
)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/current', methods=['GET'])
@login_required
def get_current_user_id():
    print('current user: ', current_user.id)
    return jsonify({'user_id': current_user.id})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid email or password'}), 401

    login_user(user)

    return jsonify({'message': 'Login successful'})


@ app.route('/logout')
@ login_required
def logout():
    logout_user()
    return redirect('/')


@ app.route('/test')
@ login_required
def test():
    return jsonify({"message": "Test Api Handler"}), 200


@ app.route("/users", methods=["POST"])
@ login_required
def create_user():
    data = request.get_json()
    data_dict = data

    user = User(name=data_dict["name"],
                email=data_dict["email"],
                )
    user.set_password(data_dict['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully.", "user_id": user.id
                    })


@ app.route('/users/<int:user_id>', methods=['GET'])
@ login_required
def get_user(user_id):

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    location_list = user.location.split('|') if user.location else []

    return jsonify({
        'user_id':user.id,
        'name': user.name,
        'email': user.email,
        'location': location_list,
        'preferred_days': user.preferred_days,
        'preferred_times': user.preferred_times,
        'interests': user.interests,
        'frequency': user.frequency,
        'paused': user.paused
    })


@app.route('/users/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.get_json()

    # Check if all required fields are present
    required_fields = ["name", "email", "paused",
                       "frequency"]
    missing_fields = []

    for field in required_fields:
        if field not in data:
            missing_fields.append(field)

    if missing_fields:
        app.logger.error('UPDATE USER MISSING FIELDS:', ', '.join(missing_fields))
        return jsonify({"message": "Bad request", "missing_fields": missing_fields}), 400

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.location = '|'.join(data.get("location", user.location))
    user.preferred_days = data.get("preferred_days", user.preferred_days)
    user.preferred_times = data.get("preferred_times", user.preferred_times)
    user.frequency = data.get("frequency", user.frequency)
    user.interests = data.get("interests", user.interests)
    user.paused = data.get("paused", user.paused)
    db.session.commit()
    return jsonify({"message": "User updated successfully."})

@app.route('/manifest.json')
def send_manifest():
    return send_from_directory('frontend/build', 'manifest.json')

@app.route('/get_matches')
def get_matches():
    matches = matches.find_matches()


if __name__ == '__main__':
    app.run(debug=True)
    # Only create the models once
    with app.app_context():
        db.create_all()
        if not db.engine.dialect.has_table(db.engine, 'users'):
            print('CREATING ALL TABLES')
            db.create_all()
