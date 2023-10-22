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
        alice = User(name='Alice', email='alice@example.com', preferred_days='MONDAY|WEDNESDSAY', preferred_times='Lunch', interests='Tech', frequency='WEEKLY')
        bob = User(name='Bob', email='bob@example.com', preferred_days='MONDAY|WEDNESDSAY', preferred_times='Lunch', interests='Tech', frequency='WEEKLY')
        charlie = User(name='Charlie', email='charlie@example.com', preferred_days='MONDAY', preferred_times=None, interests='Finance', frequency='MONTHLY')
        dave = User(name='Dave', email='dave@example.com', frequency='WEEKLY')  # No preferences specified
        juan = User(name='Juan', email='juan@example.com', frequency='WEEKLY')  # No preferences specified

        # Add test users to the database
        db.session.add(alice)
        db.session.add(bob)
        db.session.add(charlie)
        db.session.add(dave)
        db.session.commit()

        # Run the find_matches function
        got_matches = matches.match_users()
        print('GOT MATCHES: ', got_matches)

        expected_pair_1 = {alice, bob}
        expected_pair_2 = {charlie, dave}

        # Check that users with matching or wildcard preferences are paired
        self.assertTrue(expected_pair_1 in got_matches)
        self.assertTrue(expected_pair_2 in got_matches)

        expected_missing_pair1 = {alice, charlie}
        expected_missing_pair2 = {charlie, bob}

        # Check that user3 is not paired with user1 or user2 (because interests do not match)
        self.assertNotIn(expected_missing_pair1, got_matches)
        self.assertNotIn(expected_missing_pair2, got_matches)

if __name__ == '__main__':
    unittest.main()