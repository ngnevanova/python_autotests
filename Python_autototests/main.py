import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f258972a68c1a4ce7ec637325141dec0'
HEADER = {'Content-Type' : 'application/json',  'trainer_token': TOKEN}
body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_edit_pokemon = {
    "pokemon_id": "178794",
    "name": "Бульбазавр",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "178794"
}

create_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(create_pokemon.text)

edit_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_edit_pokemon)
print(edit_pokemon.text)

pokemon_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(pokemon_add_pokeball.text)