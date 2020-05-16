from datetime import datetime
from pprint import pprint

import vk
import private_settings
from datetime import  datetime


class User():
    """Клас описывает основные параметры пользователя, которые будем сохранять в базу"""

    def __init__(self, name):
        try:
            # self.TOKEN = input('Введите ваш ТОКЕН: ')
            self.TOKEN = 1
            #self.api = self.auth(self.TOKEN, name)
            self.id = self.user_info[0]['id']
            self.bdate = self.user_info[0]['bdate']
            self.sex = self.user_info[0]['sex']
            self.city = self.user_info[0]['city']
            self.music = self.user_info[0]['music']
            self.books = self.user_info[0]['books']
            self.interests = self.user_info[0]['interests']
        except KeyError as key:
            print('У пользователя отсутствует поле', key)
        except Exception as er:
            print('Введён неккоректный ID или неккоректное короткое имя.', er)
        self.prepare_to_search()

    def __str__(self):
        return str(self.user_info)

    # def auth(self, TOKEN, name):
    #     """ метод авторизации """
    #     # try:
    #     #     self.session = vk.Session(access_token=TOKEN)
    #     #     self.api = vk.API(self.session, v='5.103', lang='ru', timeout=10)
    #     #     self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    #     #     print('Введенный токен корректен - ', TOKEN)
    #     # except:
    #     #     self.session = vk.Session(access_token=private_settings.TOKEN)
    #     #     self.api = vk.API(self.session, v='5.103', lang='ru', timeout=10)
    #     #     self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    #     #     print('Введенный токен не подошёл, исопльзую по-умолчанию')
    #     self.session = vk.Session(access_token=private_settings.TOKEN)
    #     self.api = vk.API(self.session, v='5.103', lang='ru', timeout=10)
    #     self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    #     print('Введенный токен не подошёл, использую по-умолчанию')
    #     return self.api

    def prepare_to_search(self):
        """Метод проверяет все ли обязательные поля заполненны, и просит ввести вручную, если данных нет"""
        try:
            birthday = datetime.strptime(self.bdate, "%d.%m.%Y")
            age = birthday.year
            age = datetime.now().year - age
        except Exception as er:
            print(er, ' - год рождения не указан')
            age = int(input('Введите возраст кандидата: '))
        self.age = age
        self.start_age = age - 5
        self.finish_age = age + 5

    def friends(self):
        # возвращает в том порядке, в котором расположены в разделе Мои
        user_friends = self.api.friends.get(user_id=self.id, order='hints')
        return user_friends

    def friends_count(self, api):
        user_friends = User.friends(self, api)
        friends_count = len(user_friends)
        return friends_count

    # возвращает массив данных о юзере
    def info(self, api):
        user = api.users.get(user_id=self.id)
        return user[0]

    def search_users(self):
        """ Метод получает список пользователей подходящих под базовый запрос (город, диапазон возраста, статус, пол) """

        # params['count'] = [100]
        # params['status'] = [1, 6]
        if self.sex == 1:
            sex_ = 2
        else:
            sex_ = 1
        candidates = self.api.users.search(city=self.city['id'], sex=sex_, age_from=self.start_age,
                                           age_to=self.finish_age, status=1, count=50)
        candidates_items = candidates['items']
        print(candidates_items)
        candidates_ = list()
        for i in candidates_items:
            candidates_.append(i['id'])
            print(i['id'], ' - ', i['first_name'], ' ', i['last_name'], ' ', 'https://vk.com/id' + str(i['id']))
            #print(candidates['id'], candidates['last_name'], ' ', candidates['first_name'])
        return candidates_


def auth():
    """ авторизация в ВК """
    # try:
    #     self.session = vk.Session(access_token=TOKEN)
    #     self.api = vk.API(self.session, v='5.103', lang='ru', timeout=10)
    #     self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    #     print('Введенный токен корректен - ', TOKEN)
    # except:
    #     self.session = vk.Session(access_token=private_settings.TOKEN)
    #     self.api = vk.API(self.session, v='5.103', lang='ru', timeout=10)
    #     self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    #     print('Введенный токен не подошёл, исопльзую по-умолчанию')
    session = vk.Session(access_token=private_settings.TOKEN)
    api = vk.API(session, v='5.103', lang='ru', timeout=10)
    #self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    return api


def get_token():
    pass


def input_id_or_screen_name(api):
    user_input = 4298081
    # user_input = input('Введите ID или )


def get_friends_by_id(api, id):
    print(api.friends.get(user_id=id))


def get_info_by_id(api, id):
    # print(id)
    user_info = api.users.get(user_ids=id, fields='bdate, sex, home_town, interests')
    print(user_info)
    print('пол', user_info[0]['sex'])
    print('дата рождения: ', user_info[0]['bdate'])
    print('Расположение: ', user_info[0]['home_town'])
    print('Интересы: ', user_info[0]['interests'])

    user_groups = api.groups.get(user_id=id)

    print('Состоит в группах: ', user_groups['items'])


def main():
    TOKEN = get_token()
    API = auth()

    # test002 = User(test_id) #Куварин
    # test003 = User(1)
    # test004 = User(13323484) # Олег (Закрытый)

    # user_error = User('askdjfhaskdjfhsakd')
    lapssh = User('stupport')
    res = lapssh.search_users()
    print(len(res))
    print(res)
    for i in res:
        i = User(i)

    # test005 = User(4298081) #Отавина
    # test005.search_users()


if __name__ == '__main__':
    main()
