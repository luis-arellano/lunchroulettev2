from random import shuffle
from models import User, Match, Review
from itertools import combinations
from collections import defaultdict

def find_matches():
    # Retrieve all users who are not paused
    active_users = User.query.filter_by(paused=False).all()

    # Function to create preference groups
    def create_preference_groups(users):
        groups = defaultdict(set)
        for user in users:
            groups.setdefault(user.preferred_days or '*', []).append(user)
            groups.setdefault(user.preferred_times or '*', []).append(user)
            groups.setdefault(user.interests or '*', []).append(user)
        return groups

    # Create preference groups
    preference_groups = create_preference_groups(active_users)

    # Create a list of potential matches by matching users within the same group
    potential_matches = []
    for group in preference_groups.values():
        group_matches = [comb for comb in combinations(group, 2) if comb[0].id != comb[1].id]
        potential_matches.extend(group_matches)

    # Shuffle the list of potential matches to ensure randomness
    shuffle(potential_matches)

    # Select matches, making sure each user is only in one match
    matches = []
    matched_users = set()
    for match in potential_matches:
        if match[0].id not in matched_users and match[1].id not in matched_users:
            matches.append(match)
            matched_users.add(match[0].id)
            matched_users.add(match[1].id)

    return matches