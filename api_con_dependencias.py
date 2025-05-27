import requests

api = "https://pokeapi.co/api/v2/ability/1/"

response = requests.get(api)
print(response.json())

response = requests.post("https://pokeapi.co/api/v2/ability/1/", json={"name": "en"})
response.