# Написать программу, которая будет выводить топ 10 самых часто встречающихся
# в новостях слов длиннее 6 символов для каждого файла.
import json
from pprint import pprint

def read_json(filename):
    json_data = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    #pprint(json_data)
    return json_data

def take_news(text):
    root = text['rss']['channel']['items']
    news = ''
    for one_news in root:
        news = news + '\n' + one_news['description']
    return news

def get_top_10_words(news):
    word_list = news.split()
    big_word_list = list()
    for word in word_list:
        if len(word) > 6:
            big_word_list.append(word)
    sorted_words_list = sorted(big_word_list)
    print(sorted_words_list)

def print_top_10_words(top10):
    pass

filename = 'newsafr.json'
json_data = read_json(filename)
news = take_news(json_data)
top10_words = get_top_10_words(news)
test_list = [
    [10,'mama'],
    [120, 'papa'],
    [1, 'peresvet'],
    [12, 'maya']
]
print(test_list.sort())