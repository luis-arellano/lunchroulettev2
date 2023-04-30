from flask import Flask, request, jsonify, session, redirect, send_from_directory, make_response, render_template
from flask import Response
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from models import User, Match, Review
from create_app import app, db
from flask_cors import CORS  # comment this on deployment
import json

# Initialize the database
db.init_app(app)

# CORS(app)  # comment this on deployment
CORS(app, supports_credentials=True)

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


@app.route('/')
def index():
    # print('current user: ', current_user.is_authenticated)
    return render_template('index.html')
    # return ("Welcome to Lunch Roulette")


@app.route('/get_current_user_id', methods=['GET'])
@login_required
def get_current_user_id():
    response = Response(jsonify({'user_id': current_user.id}), 200)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response, 200


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
    print('current user: ', current_user)
    print('Authen: ', current_user.is_authenticated)

    response = jsonify({'message': 'Login successful'})
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Origin',
                         request.headers.get('Origin'))
    print(response)
    return response, 200


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


@ app.route('/get_user/<int:user_id>', methods=['GET'])
@ login_required
def get_user(user_id):

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        'name': user.name,
        'email': user.email,
        'location': user.location,
        'preferred_days': user.preferred_days,
        'preferred_times': user.preferred_times,
        'interests': user.interests,
        'frequency': user.frequency,
        'paused': user.paused
    })


@ app.route('/update_user/<int:user_id>', methods=['POST'])
@ login_required
def update_user(user_id):
    data = request.get_json()

    # Check if all required fields are present
    required_fields = ["name", "email", "location",
                       "preferred_days", "preferred_times"]
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Bad request"}), 400

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.location = data.get("location", user.location)
    user.preferred_days = data.get("preferred_days", user.preferred_days)
    user.preferred_times = data.get("preferred_times", user.preferred_times)
    user.frequency = data.get("frequency", user.frequency)
    user.interests = data.get("interests", user.interests)
    user.paused = data.get("paused", user.paused)
    db.session.commit()
    return jsonify({"message": "User updated successfully."})


if __name__ == '__main__':
    app.run(debug=True)
    # Only create the models once
    with app.app_context():
        db.create_all()
        if not db.engine.dialect.has_table(db.engine, 'user'):
            print('CREATING ALL TABLES')
            db.create_all()
