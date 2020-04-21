import OAUTH_TOKEN
import requests
import json

TOKEN = OAUTH_TOKEN.OAUTH_TOKEN
API_KEY = OAUTH_TOKEN.API_KEY
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang, to_lang='ru'):
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


    params = {
        'key': API_KEY,
        'text': text,
        'lang': from_lang + '-' + to_lang
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return json_

if __name__ == '__main__':
    from_lang = 'en'
    json_response = translate_it('hello', from_lang)
    print('Исходное слово: hello. Перевод: ',json_response['text'][0])
    print('Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru.')
    print(json_response)
    print(json_response['code'])
    print(json_response['text'][0])

