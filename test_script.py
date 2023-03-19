import requests
import json
import os

BASE = "http://127.0.01:5000/"

payload = json.dumps({
    "name": "John Doe",
    "email": "johndoe@example.com",
    "location": "San Francisco",
    "preferred_days": "MONDAY|TUESDAY",
    "preferred_times": "12:30 - 13:30",
    "frequency": "weekly",
})

# Make a post request
post_response = requests.post(BASE + "users", json=payload)

# Make a get request
get_response = requests.get(BASE + "get_user/1")


print('URI ', os.environ.get('DATABASE_URI'))
print('POST RESPONSE', post_response.json())
print('GET RESPONSE', get_response.json())
