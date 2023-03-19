# Models for entities
from create_app import db
# from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    preferred_days = db.Column(db.String(120), nullable=False)
    preferred_times = db.Column(db.String(120), nullable=False)
    frequency = db.Column(db.String(120), nullable=False)
    interests = db.Column(db.String(120), nullable=True)
    paused = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    user_ids = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Match %r>' % self.id


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.id
