import requests

URL = 'http://127.0.0.1:8000/protocol/new'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

protocol = [
    {
    "user_id": 1
  },
  {
    "user_id": 2
  },
  {
    "user_id": 3
  },
]

for item in protocol:
    data = item
    requests.post(URL, headers=headers, json=data)