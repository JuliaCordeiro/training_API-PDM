import requests

URL = 'http://127.0.0.1:8000/training/new'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

training = [
  {
    "protocol_id": 1,
    "muscle_group": 1
  },
  {
    "protocol_id": 1,
    "muscle_group": 2
  },
  {
    "protocol_id": 1,
    "muscle_group": 6
  },

  {
    "protocol_id": 2,
    "muscle_group": 1
  },
  {
    "protocol_id": 2,
    "muscle_group": 2
  },
  {
    "protocol_id": 2,
    "muscle_group": 3
  },
  {
    "protocol_id": 2,
    "muscle_group": 4
  },
  {
    "protocol_id": 2,
    "muscle_group": 6
  },
  
  {
    "protocol_id": 3,
    "muscle_group": 1
  },
  {
    "protocol_id": 3,
    "muscle_group": 2
  },
  {
    "protocol_id": 3,
    "muscle_group": 3
  },
  {
    "protocol_id": 3,
    "muscle_group": 4
  },
  {
    "protocol_id": 3,
    "muscle_group": 5
  },
  {
    "protocol_id": 3,
    "muscle_group": 6
  }
]

# BACK(1),
# CHEST(2),
# BICEPS(3),
# TRICEPS(4),
# SHOULDER(5),
# LEGS(6);

for item in training:
    data = item
    requests.post(URL, headers=headers, json=data)