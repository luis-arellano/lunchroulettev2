from flask import Flask, request, jsonify, session, redirect, send_from_directory, make_response, render_template, session
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from create_app import app, db
from flask_cors import CORS  # comment this on deployment
import json

from sqlalchemy.sql import func

from datetime import datetime, timezone, timedelta

from functools import wraps

from flask import request
from flask_restx import Api, Resource, fields

import jwt

from models import db, User, JWTTokenBlocklist

import requests

rest_api = Api(version="1.0", title="Users API")

# CORS(app)  # comment this on deployment
CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = '36&462134kjKDhuIS_d23'
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=False,
    SESSION_COOKIE_SAMESITE=None
)


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if "authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return {"success": False, "msg": "Valid JWT token is missing"}, 400

        try:
            data = jwt.decode(token, 'secret',
                              algorithms=["HS256"])
            current_user = User.get_by_email(data["email"])

            if not current_user:
                return {"success": False,
                        "msg": "Sorry. Wrong auth token. This user does not exist."}, 400

            token_expired = db.session.query(
                JWTTokenBlocklist.id).filter_by(jwt_token=token).scalar()
            print("sdsdsdsd~", token_expired)

            if token_expired is not None:
                return {"success": False, "msg": "Token revoked."}, 400

            if not current_user.check_jwt_auth_active():
                return {"success": False, "msg": "Token expired."}, 400
        except:
            return {"success": False, "msg": "Token is invalid"}, 400

        return f(current_user, *args, **kwargs)

    return decorator

@app.route('/login', methods=['POST'])
def login():

    req_data = request.get_json()
    _email = req_data.get("email")
    _password = req_data.get("password")

    user_exists = User.get_by_email(_email)
    print(user_exists)
    if not user_exists:
        return {"success": False,
                "msg": "This email does not exist."}, 400

    if not user_exists.check_password(_password):
        return {"success": False,
                "msg": "Wrong credentials."}, 400

    # create access token uwing JWT
    token = jwt.encode({'email': _email, 'exp': datetime.utcnow(
    ) + timedelta(minutes=30)}, 'secret')

    user_exists.set_jwt_auth_active(True)
    user_exists.save()

    return {"success": True,
            "token": token,
            "user": user_exists.to_json()}, 200


@app.route('/get_current_user_id', methods=['GET'])
@token_required
def get_current_user_id(current_user):
    return jsonify({"user_id": current_user.id})


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


@app.route('/update_user', methods=['POST'])
@token_required
def update_user(self, current_user):
    data = request.get_json()

    # Check if all required fields are present
    required_fields = ["name", "email", "location",
                       "preferred_days", "preferred_times"]
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Bad request"}), 400

    '''
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
    '''
    return jsonify({"message": "User updated successfully."})


@app.route('/logout')
@token_required
def post(current_user):
    _jwt_token = request.headers["authorization"]

    jwt_block = JWTTokenBlocklist(
        jwt_token=_jwt_token, created_at=datetime.now(timezone.utc))
    jwt_block.save()

    current_user.set_jwt_auth_active(False)
    current_user.save()
    return jsonify({"success": True})
