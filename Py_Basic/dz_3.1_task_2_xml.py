# Написать программу, которая будет выводить топ 10 самых часто встречающихся
# в новостях слов длиннее 6 символов для каждого файла.
import xml.etree.ElementTree as ET
import pprint

def read_xml(filename): # Считываем данные из переданного xml файла
    tree = ET.parse(filename)
    root = tree.getroot()
    items = root.findall('channel/item')
    news = ''
    for item in items:
        news = news + '\n' +item.find('description').text

    return news


def get_top_10_words(news): # отбираем топ 10 слов длиннее 6 символов
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
    # Получаем слово с максимальным счетчиком, вносим в топ и удаляем из словаря.
    for i in range (10):
        max_value = max(words_counter.values())
        final_dict = [k for k, v in words_counter.items() if v == max_value]
        top10_words_list.append([final_dict[0], max_value])
        del words_counter[top10_words_list[-1][0]]

    return top10_words_list

def print_top_10_words(top10):
    print('Внимательно и вдумчиво изучив все африканские новости, мы пришли к выводу,\n'
          'что чаще всего в новостях встречются следующие 10 слов:\n')
    for i in top10:
        print(f'Слово "{i[0]}" встречалось {i[1]} раз')

filename = 'newsafr.xml'
news = read_xml(filename)
top10_words = get_top_10_words(news)
print_top_10_words(top10_words)
