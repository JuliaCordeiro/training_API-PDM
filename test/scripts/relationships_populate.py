import requests

URL = 'http://127.0.0.1:8000/relationships/new'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

relationship = [
  {
    "training_id": 1,
    "exercise_id": 1
  },
  {
    "training_id": 2,
    "exercise_id": 7
  },
  {
    "training_id": 3,
    "exercise_id": 21
  },

  {
    "training_id": 4,
    "exercise_id": 2
  },
  {
    "training_id": 5,
    "exercise_id": 8
  },
  {
    "training_id": 6,
    "exercise_id": 10
  },
  {
    "training_id": 7,
    "exercise_id": 12
  },
  {
    "training_id": 8,
    "exercise_id": 22
  },
  
  {
    "training_id": 9,
    "exercise_id": 3
  },
  {
    "training_id": 10,
    "exercise_id": 9
  },
  {
    "training_id": 11,
    "exercise_id": 11
  },
  {
    "training_id": 12,
    "exercise_id": 14
  },
  {
    "training_id": 13,
    "exercise_id": 17
  },
  {
    "training_id": 14,
    "exercise_id": 23
  },

  {
    "training_id": 1,
    "exercise_id": 2
  },
  {
    "training_id": 2,
    "exercise_id": 8
  },
  {
    "training_id": 3,
    "exercise_id": 22
  },

  {
    "training_id": 4,
    "exercise_id": 3
  },
  {
    "training_id": 5,
    "exercise_id": 7
  },
  {
    "training_id": 6,
    "exercise_id": 11
  },
  {
    "training_id": 7,
    "exercise_id": 13
  },
  {
    "training_id": 8,
    "exercise_id": 24
  },
  
  {
    "training_id": 9,
    "exercise_id": 4
  },
  {
    "training_id": 10,
    "exercise_id": 8
  },
  {
    "training_id": 11,
    "exercise_id": 10
  },
  {
    "training_id": 12,
    "exercise_id": 15
  },
  {
    "training_id": 13,
    "exercise_id": 18
  },
  {
    "training_id": 14,
    "exercise_id": 24
  }
]

for item in relationship:
    data = item
    requests.post(URL, headers=headers, json=data)
