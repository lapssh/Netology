import requests
import OAuth_TOKEN
from pprint import pprint

# функция загрузки файлов
def upload(file_name):
    TOKEN = OAuth_TOKEN.get_token()
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {
        'path' : 'translate_files/' + file_name,
        'overwrite': 'True'
    }
    headers = {'Authorization': TOKEN,
               'Accept': 'application/json',
               }

    path_file = 'recipes.txt'
    request = requests.get(url, params=params, headers=headers)
    URL = request.json()['href']
    print(URL)
    with open(path_file, 'rb') as d_file:
        data = d_file.read()
        res = requests.put(URL, data=data)
        print(f'Файл: {path_file} скопирован на Яндекс.Диск {res}\n')
        print('Доступно по этому адресу: https://yadi.sk/d/g-8c6xyTb7egjA')
        pprint(res.text)
        print(res.status_code)

file_name = 'recipes.txt'
upload(file_name)
