import unittest
import matches
from create_app import app, db
from models import User


class FindMatchesTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_find_matches(self):
        # Create test users
        user1 = User(name='Alice', email='alice@example.com', preferred_days='Mon,Wed', preferred_times='Lunch', interests='Tech')
        user2 = User(name='Bob', email='bob@example.com', preferred_days='Mon,Wed', preferred_times='Lunch', interests='Tech')
        user3 = User(name='Charlie', email='charlie@example.com', preferred_days='Mon', preferred_times='Lunch', interests='Finance')
        user4 = User(name='Dave', email='dave@example.com')  # No preferences specified

        # Add test users to the database
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)
        db.session.commit()

        # Run the find_matches function
        got_matches = matches.find_matches()
        print('GOT MATCHES: ', got_matches)


        # Check that users with matching or wildcard preferences are paired
        self.assertIn(((user1, user2) or (user2, user1)), got_matches)
        self.assertIn(((user1, user4) or (user4, user1)), got_matches)
        self.assertIn(((user2, user4) or (user4, user2)), got_matches)
        self.assertIn(((user3, user4) or (user4, user3)), got_matches)

        # Check that user3 is not paired with user1 or user2 (because interests do not match)
        self.assertNotIn(((user3, user1) or (user1, user3)), got_matches)
        self.assertNotIn(((user3, user2) or (user2, user3)), got_matches)

if __name__ == '__main__':
    unittest.main()