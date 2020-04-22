import OAUTH_TOKEN
import requests
import json


class TranslateMe:

    def __init__(self, name, text, from_lang='en', to_lang='ru'):
        self.name = name
        self.text = text
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.TOKEN = OAUTH_TOKEN.OAUTH_TOKEN
        self.API_KEY = OAUTH_TOKEN.API_KEY
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.params = {
            'key': self.API_KEY,
            'text': self.text,
            'lang': self.from_lang + '-' + self.to_lang
        }

    def translate_it(self):
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
        self.response = requests.get(self.URL, params=self.params)
        self.json_ = self.response.json()
        return self.json_


if __name__ == '__main__':
    zapros01 = TranslateMe('zapros01', 'hello', to_lang='de')
    print(zapros01.translate_it())
    zapros02 = TranslateMe('zapros02', 'Di katze', from_lang='de')
    print(zapros02.translate_it())
