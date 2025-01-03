import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f258972a68c1a4ce7ec637325141dec0'
HEADER = {'Content-Type' : 'application/json',  'trainer_token': TOKEN}
TRAINER_ID = 4434

def test_status_code():
    response_status = requests.get(url=f'{URL}/trainers' )
    assert response_status.status_code == 200

def test_part_of_response():
    response_get_name = requests.get(url=f'{URL}/me' ,headers = HEADER)
    assert response_get_name.json()['data'][0]["trainer_name"] == 'Наталья'
