# Models for entities
from create_app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))  # Add this line
    location = db.Column(db.String(120), nullable=True)
    preferred_days = db.Column(db.String(120), nullable=True)
    preferred_times = db.Column(db.String(120), nullable=True)
    frequency = db.Column(db.String(120), nullable=True)
    interests = db.Column(db.String(120), nullable=True)
    paused = db.Column(db.Boolean, default=False)
    is_matched = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.name


class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    user_ids = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=True)
    time = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Match %r>' % self.id


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.id
