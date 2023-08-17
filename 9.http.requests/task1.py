import requests
from pprint import pprint

ROOT_API_PATH = 'https://superheroapi.com/api/2619421814940190/'
heroes = ['Hulk', 'Captain America', 'Thanos']

def get_hero_id(hero_name: str):
    resp = requests.get(f'{ROOT_API_PATH}/search/{hero_name}')
    resp.raise_for_status()
    return resp.json()['results'][0]['id']


def get_hero_intelligence(hero_name: str):
    hero_id = get_hero_id(hero_name)
    resp = requests.get(f'{ROOT_API_PATH}/{hero_id}/powerstats')
    resp.raise_for_status()
    return resp.json()['intelligence']


def build_her_list(heroes):
    heroes_list: list = list()
    for hero in heroes:
        heroes_list.append({'name': hero, 'id': get_hero_id(hero), 'intelligence': get_hero_intelligence(hero)})
    return heroes_list

her_list = build_her_list(heroes)
her_list.sort(key=(lambda x:int(x['intelligence'])), reverse=True)
print(her_list)