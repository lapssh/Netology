#  AgAAAAAjPcXKAADLW2Vd5_LN5kb3qIhAlLj4hcc
import requests
from pprint import pprint
OAUTH_TOKEN = 'AgAAAAAjPcXKAADLW2Vd5_LN5kb3qIhAlLj4hcc'
# функция загрузки файлов
def upload(file_name):
    pprint('ест принта')
    url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_name}'
    headers = {'Authorization': OAUTH_TOKEN,
               'Accept': 'application/json',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    session = requests.Session()
    request = session.get(url, headers=headers)
    pprint(request.text)
    print(request.status_code)

#res = requests.get(URL + '/v1/disk/resources/upload?test.txt', params=params)
file_name = 'recipes.txt'
upload(file_name)
