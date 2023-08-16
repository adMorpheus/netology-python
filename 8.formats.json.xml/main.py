import json
import xml.etree.ElementTree as ET
from pprint import pprint


def get_json_news(src_file):
    with open(src_file, encoding='utf-8') as file:
        json_data = json.load(file)
    items = json_data['rss']['channel']['items']
    full_text = ''
    for item in items:
        full_text += item['description']
    return full_text


def get_xml_news(file):
    result_data = ''
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file, parser)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    for xml_item in xml_items:
        result_data += xml_item.find('description').text

    return result_data


def del_short_words(text, lenght):
    result_text = ''
    for word in text.split():
        if len(word) > int(lenght): result_text += f'{word} '
    return result_text


def get_statistic(data, count):
    word_map = {}
    for word in data.split():
        if word in word_map.keys():
            word_map[word] += 1
        else:
            word_map[word] = 1
    top_count = sorted(word_map.values(), reverse=True)[:count]
    result_list = list()
    for item in word_map.keys():
        if word_map[item] in top_count:
            result_list.append(item)
    top = list()
    for lead_word in result_list:
        lead_word = f'{str(data.count(lead_word))}: {lead_word}'
        top.append(lead_word)
    return sorted(top, reverse=True)


all_json_data = get_json_news('newsafr.json')
filtred_json_data = del_short_words(all_json_data, 6)
print(get_statistic(filtred_json_data, 10))

all_xml_data = get_xml_news('newsafr.xml')
filtred_xml_data = del_short_words(all_xml_data, 6)
print(get_statistic(filtred_xml_data, 10))
print(filtred_xml_data == filtred_json_data)
