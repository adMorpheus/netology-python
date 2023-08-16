import json
from pprint import pprint


def get_json_news(src_file):
    with open(src_file, encoding='utf-8') as file:
        json_data = json.load(file)
    items = json_data['rss']['channel']['items']
    full_text = ''
    for item in items:
        full_text += item['description']
    return full_text


def get_xml_news(files):
    pass


def get_statistic(data):
    pass


get_json_news('newsafr.json')
