import requests
import os
import OAUTH_TOKEN

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def get_path_file_name(file_name, path):
    """
    Функция получения православного пути файла
    адекватно работает в любых операционных системах
    """
    file1name = os.path.join(path, file_name)
    file2name = os.path.join(path, 'translate-' + file_name)
    return file1name, file2name

def upload(file_name):
    """
    Функция загружает переданный файл на Яндекс.Диск
    """
    TOKEN = OAUTH_TOKEN.OAUTH_TOKEN
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {
        'path' : 'translate_files/' + file_name,
        'overwrite': 'True'
    }
    headers = {'Authorization': TOKEN,
               'Accept': 'application/json',
               }

    request = requests.get(url, params=params, headers=headers)
    URL = request.json()['href']
    with open(file_name, 'rb') as d_file:
        data = d_file.read()
        res = requests.put(URL, data=data)
        print(f'Файл: {file_name} скопирован на Яндекс.Диск')
        print('Рузельтат перевода доступен по этому адресу: https://yadi.sk/d/g-8c6xyTb7egjA')
        print()


def translate_it(file_name_gibberish, file_name_translate, from_lang, to_lang = 'ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    print('Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru.')
    with open(file_name_gibberish, encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': from_lang + '-' + to_lang
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    with open(file_name_translate, 'w', encoding='utf-8') as f:
        f.write(''.join(json_['text']))
    print(file_name_translate)
    upload(file_name_translate)
    return

path = 'files'
file_name = 'DE.txt'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'de', 'ru')

file_name = 'FR.txt'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'fr', 'ru')

file_name = 'ES.txt'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'es')
