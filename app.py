from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import User, Match, Review
from create_app import app, db
from flask_cors import CORS  # comment this on deployment
import json

# Initialize the database
db.init_app(app)

CORS(app)  # comment this on deployment


@app.route('/')
def index():
    return ("Welcome to Lunch Roulette")


@app.route('/test')
def test():
    return jsonify({"message": "Test Api Handler"}), 200


@app.route("/users", methods=["POST"])
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


@app.route('/get_user/<int:user_id>', methods=['GET'])
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


@app.route('/update_user/<int:user_id>', methods=['POST'])
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
