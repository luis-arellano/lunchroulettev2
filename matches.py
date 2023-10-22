from random import shuffle
from models import User, Match, Review
from datetime import datetime, timedelta
from create_app import app, db

# from itertools import combinations
# from collections import defaultdict
# from pprint import pprint

def get_recent_matches_for_user(user_id):
    ''' Return recent matches for a user based on their frequency preference. '''
    user = User.query.get(user_id)

    time_thresholds = {
        'MULTIPLE': timedelta(days=3.5),
        'WEEKLY': timedelta(days=7),
        'FORTHNIGHTLY': timedelta(days=14),
        'MONTHLY': timedelta(days=30)
    }
    time_threshold = time_thresholds.get(user.frequency)
    
    return Match.query.filter(
        Match.user_ids.contains(str(user_id)),
        Match.date >= (datetime.now() - time_threshold).date()
    ).all()

def match_users():
    # Fetch all users who are not paused
    active_users = User.query.filter_by(paused=False).all()

    frequency_order = ['MULTIPLE', 'WEEKLY', 'FORTHNIGHTLY', 'MONTHLY']
    sorted_users = sorted(active_users, key=lambda x: frequency_order.index(x.frequency or 'WEEKLY'))

    matches = []
    while sorted_users:
        user = sorted_users.pop(0)
        print('looking for: ', user)
        recent_matches = get_recent_matches_for_user(user.id)
        print('recent matches: ', recent_matches)
        
        # Check if the user has been matched as per their frequency preference
        if len(recent_matches) >= frequency_order.index(user.frequency):
            continue

        for potential_match in sorted_users:
            # Match by location
            user_locations = set(user.location.split(',')) if user.location else set()
            potential_match_locations = set(potential_match.location.split(',')) if potential_match.location else set()

            if user_locations and potential_match_locations and not user_locations.intersection(potential_match_locations):
                continue
            
            # Match by preferred days
            if user.preferred_days and potential_match.preferred_days:
                user_days = set(user.preferred_days.split(','))
                match_days = set(potential_match.preferred_days.split(','))
                if not user_days.intersection(match_days):
                    continue

            # If all checks passed, they are a match
            matches.append({user, potential_match})
            print('FOUND MATCH: ', potential_match)
            
            # Record match in the Match table
            new_match = Match(
                user_ids=f"{user.id},{potential_match.id}",
                location=user.location or potential_match.location,
                time=datetime.now().time(),
                date=datetime.now().date()
            )

            # TODO(add matches to the db)
            # db.session.add(new_match)
            # db.session.commit()

            sorted_users.remove(potential_match)
            break
    print('FULL MATCHES: ', matches)
    return matches