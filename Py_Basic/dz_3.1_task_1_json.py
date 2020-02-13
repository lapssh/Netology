# Написать программу, которая будет выводить топ 10 самых часто встречающихся
# в новостях слов длиннее 6 символов для каждого файла.
import json

def read_json(filename):
    json_data = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
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
    #создаем словарь формата СЛОВО : количество вхождений
    words_counter = dict()
    for word in sorted_words_list:
        if word not in words_counter:
            words_counter[word] = 1
        else:
            words_counter[word] += 1
    # Создаем пустой список для ТОП10 слов
    top10_words_list = list()

    # Получаем слово с максимальным счетчиком, вносим в топ и удаляем изх словаря.
    for i in range (10):
        max_value = max(words_counter.values())
        final_dict = [k for k, v in words_counter.items() if v == max_value]
        top10_words_list.append([final_dict[0], max_value])
        del words_counter[top10_words_list[-1][0]]

    return top10_words_list, words_counter

def print_top_10_words(top10,words_counter):
    print('Внимательно и вдумчиво изучив все африканские новости, мы пришли к выводу,\n'
          'что чаще всего в новостях встречются следующие 10 слов:\n')
    for i in top10:
        print(f'Слово "{i[0]}" встречалось {i[1]} раз')

filename = 'newsafr.json'
json_data = read_json(filename)
news = take_news(json_data)
top10_words, words_counter = get_top_10_words(news)
print_top_10_words(top10_words,words_counter)
