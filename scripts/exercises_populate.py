import requests

URL = 'http://127.0.0.1:8000/exercises/new'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

exercises = [
	{
		"name": "Remada Baixa",
		"muscle_type": 1,
		"level": 1
	},
	{
		"name": "Remada Curvada",
		"muscle_type": 1,
		"level": 2
	},
	{
		"name": "Remada Cerrote",
		"muscle_type": 1,
		"level": 3
	},
	{
		"name": "Puxador Frente",
		"muscle_type": 1,
		"level": 1
	},
	{
		"name": "Puxador Triângulo",
		"muscle_type": 1,
		"level": 1
	},
	{
		"name": "Puxador Fechado",
		"muscle_type": 1,
		"level": 2
	},
	{
		"name": "Supino Reto",
		"muscle_type": 2,
		"level": 2 
	},
	{
		"name": "Supino Inclinado",
		"muscle_type": 2,
		"level": 2
	},
	{
		"name": "Crossover",
		"muscle_type": 2,
		"level": 3
	},
	{
		"name": "Rosca Direta",
		"muscle_type": 3,
		"level": 1
	},
	{
		"name": "Rosca Alternada",
		"muscle_type": 3,
		"level": 2
	},
	{
		"name": "Pulley Corda",
		"muscle_type": 4,
		"level": 1
	},
	{
		"name": "Pulley Barra",
		"muscle_type": 4,
		"level": 1
	},
	{
		"name": "Barra Paralela",
		"muscle_type": 4,
		"level": 3
	},
	{
		"name": "Triceps Supinado",
		"muscle_type": 4,
		"level": 3
	},
	{
		"name": "Coice",
		"muscle_type": 4,
		"level": 2
	},
	{
		"name": "Desenvolvimento Elevação Lateral",
		"muscle_type": 5,
		"level": 1
	},	
	{
		"name": "Desenvolvimento Arnold",
		"muscle_type": 5,
		"level": 1
	},
	{
		"name": "Remada Alta",
		"muscle_type": 5,
		"level": 2
	},
	{
		"name": "Desenvolvimento",
		"muscle_type": 5,
		"level": 1
	},
	{
		"name": "Agachamento Livre",
		"muscle_type": 6,
		"level": 1
	},
	{
		"name": "Leg Press",
		"muscle_type": 6,
		"level": 1
	},
	{
		"name": "Cadeira Extensora",
		"muscle_type": 6,
		"level": 1
	},
	{
		"name": "Cadeira Flexora",
		"muscle_type": 6,
		"level": 1
	},
	{
		"name": "Mesa Flexora",
		"muscle_type": 6,
		"level": 1
	},
	{
		"name": "Panturrilha",
		"muscle_type": 6,
		"level": 1
	}
]

for item in exercises:
    data = item
    requests.post(URL, headers=headers, json=data)

# curl -X 'POST' \
#   'http://127.0.0.1:8000/exercises/new' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "string",
#   "muscle_type": 0,
#   "level": 0
# }'
