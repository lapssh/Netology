import requests
import os
#  API диска  с полигона AgAAAAAjPcXKAADLW2Vd5_LN5kb3qIhAlLj4hcc
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def get_path_file_name(file_name, path):
    file1name = os.path.join(path, file_name)
    file2name = os.path.join(path, 'translate-' + file_name)
    return file1name, file2name

def translate_it(file_name_gibberish, file_name_reult, from_lang, to_lang = 'ru'):
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
    with open(file_name_gibberish) as f:
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
    return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически
# определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

# if __name__ == '__main__':
#     print(translate_it('привет', 'en'))
file_name = 'text.txt'
path = 'files'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'ru', 'en')

file_name = 'DE.txt'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'de', 'ru')

file_name = 'FR.txt'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'fr', 'ru')

file_name = 'ES.txt'
file_name_gibberish, file_name_translate = get_path_file_name(file_name, path)
translate_it(file_name_gibberish, file_name_translate, 'es')
