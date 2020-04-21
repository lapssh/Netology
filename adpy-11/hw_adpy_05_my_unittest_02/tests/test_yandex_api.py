import unittest
import main
import OAUTH_TOKEN



class YandexTestCase(unittest.TestCase):

    def setUp(self):
        self.TOKEN = OAUTH_TOKEN.OAUTH_TOKEN
        self.API_KEY = OAUTH_TOKEN.API_KEY
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.params = {
            'key': API_KEY,
            'text': text,
            'lang': from_lang + '-' + to_lang
        }

    def test_get_response(self):
        self.assertEqual(main.translate_it('hello', from_lang)['text'][0], 'привет')


if __name__ == '__main__':
    unittest.main()
