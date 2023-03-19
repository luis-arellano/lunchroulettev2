import unittest
from flask import json
from app import app
from create_app import db
from flask_sqlalchemy import SQLAlchemy
from models import User


def _CreateUser():
    return User(name="John Doe",
                email="johndoe@example.com",
                location="San Francisco",
                preferred_days="MONDAY|TUESDAY",
                preferred_times="12:30 - 13:30",
                frequency="weekly",
                interests="soccer"
                )


class LunchRouletteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.db = db
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_create_user(self):
        user_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "location": "San Francisco",
            "preferred_days": "MONDAY|TUESDAY",
            "preferred_times": "12:30 - 13:30",
            "frequency": "weekly",
        }
        response = self.app.post(
            "/users", data=json.dumps(user_data), content_type='application/json')
        print('NEW USER ::', response.get_data())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn("User created successfully.", data["message"])

    def test_update_user(self):
        new_user = _CreateUser()
        self.db.session.add(new_user)
        self.db.session.commit()
        new_user_id = new_user.id

        update_data = {
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "location": "San Francisco",
            "preferred_days": "MONDAY|TUESDAY",
            "preferred_times": "18:00 - 19:00",
            "frequency": "weekly",
            "interests": "climbing",
            "paused": True
        }
        response = self.app.post(
            "/update_user/{0}".format(new_user_id), data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn("User updated successfully.", data["message"])

    def test_get_user(self):

        new_user = _CreateUser()
        self.db.session.add(new_user)
        self.db.session.commit()
        new_user_id = new_user.id

        response = self.app.get("/get_user/{0}".format(new_user_id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn("John Doe", data["name"])
        self.assertIn("johndoe@example.com", data["email"])
        self.assertIn("MONDAY|TUESDAY", data["preferred_days"])
        self.assertIn("12:30 - 13:30", data["preferred_times"])
        self.assertIn("San Francisco", data["location"])
        self.assertIn("weekly", data["frequency"])
        self.assertIn("soccer", data["interests"])
        self.assertEqual(False, data["paused"])


if __name__ == '__main__':
    unittest.main()
