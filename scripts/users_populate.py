import requests

URL = 'http://127.0.0.1:8000/users/new'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

users = [
    {
    "full_name": "teste iniciante",
    "activity_leveling": 1,
    "gender": 1,
    "weight": 50,
    "height": 1.70,
    "username": "iniciante",
    "password": "123"
  },
  {
    "full_name": "teste intermediário",
    "activity_leveling": 2,
    "gender": 1,
    "weight": 75,
    "height": 1.70,
    "username": "intermediario",
    "password": "123"
  },
  {
    "full_name": "teste avançado",
    "activity_leveling": 3,
    "gender": 1,
    "weight": 90,
    "height": 1.70,
    "username": "avançado",
    "password": "123"
  }
]

for item in users:
    data = item
    requests.post(URL, headers=headers, json=data)