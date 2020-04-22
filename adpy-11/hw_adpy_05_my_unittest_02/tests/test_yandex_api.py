import unittest
import main
import OAUTH_TOKEN
from main import TranslateMe


class YandexTestCase(unittest.TestCase):

    def setUp(self):
        self.translateme = TranslateMe

    def test_translate01(self):
        a1 = self.translateme('a1', 'big')
        response_a1 = a1.translate_it()
        self.assertEqual(response_a1['text'][0], 'большой')
        self.assertEqual(response_a1['code'], 200)


    def test_translate02(self):
        a2 = self.translateme('a2', 'small')
        response_a2 = a2.translate_it()
        self.assertEqual(response_a2['text'][0], 'небольшой')
        self.assertEqual(response_a2['code'], 200)

    def test_negative01(self):
        n1 = self.translateme('n1', 'lfsgdl;kfgdl;kf')
        response_n1 = n1.translate_it()
        self.assertNotEqual(response_n1['text'][0], 'осмысленный ответ')
        self.assertEqual(response_n1['code'], 200)

    def test_negative02(self):
        n2 = self.translateme('n2', 'привет')
        response_n2 = n2.translate_it()
        self.assertNotEqual(response_n2['text'][0], 'hello')
        self.assertEqual(response_n2['code'], 200)

if __name__ == '__main__':
    unittest.main()
