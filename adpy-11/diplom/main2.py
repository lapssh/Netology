from datetime import datetime
from pprint import pprint

import vk
import private_settings
from datetime import datetime
import time


class User():
    """Клас описывает основные параметры пользователя, которые будем сохранять в базу"""

    def __init__(self, name, api):
        self.api = api
        self.name = name
        self.get_data()


    def __str__(self):
        print()
        print(self.id, ' - ')
        print('Музыка: ', self.music)
        print('Книги: ', self.books)
        print('Интересы: ', self.interests)
        print('Город: ', self.city)
        print()
        return str(self.user_info)

    def get_data(self):
        self.user_info = self.api.users.get(user_ids=self.name, fields='bdate, sex, city, books, music, interests')
        self.id = self.user_info[0]['id']
        self.sex = self.user_info[0]['sex']
        if 'city' not in self.user_info[0]:
            self.city = False
        else:
            self.city = self.user_info[0]['city']
        self.city = self.user_info[0]['city']
        if 'music' not in self.user_info[0]:
            self.music = False
        else:
            self.music = self.user_info[0]['music']
        if 'books' not in self.user_info[0]:
            self.books = False
        else:
            self.books = self.user_info[0]['books']
        if 'interests' not in self.user_info[0]:
            self.interests = False
        else:
            self.interests = self.user_info[0]['interests']
        if 'bdate' not in self.user_info[0]:
            self.bdate = False
            self.age = False
            print('У ', self.name, ' появился ', self.bdate)
        else:
            self.bdate = self.user_info[0]['bdate']
            try:
                birthday = datetime.strptime(self.bdate, "%d.%m.%Y")
                age = birthday.year
                self.age = datetime.now().year - age
            except:
                self.age = False

        # except KeyError as key:
        #     print('У пользователя отсутствует поле', key)
        # except Exception as er:
        #     print('Введён неккоректный ID или неккоректное короткое имя.', er)


    def get_mutual(self, target):
        #target = int(target)
        time.sleep(0.4)
        try:
            self.mutual_friends = self.api.friends.getMutual(source_uid=self.id, target_uid=target)
        except Exception as err:
            print('Профиль ', self.id, ' закрыт, данные не получены')
            self.mutual_friends = False

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
                                           age_to=self.finish_age, status=[1], count=255)
        candidates_items = candidates['items']
        print(candidates_items)
        candidates_ = list()
        for i in candidates_items:
            candidates_.append(i['id'])
            print(i['id'], ' - ', i['first_name'], ' ', i['last_name'], ' ', 'https://vk.com/id' + str(i['id']))
            # print(candidates['id'], candidates['last_name'], ' ', candidates['first_name'])
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
    # self.user_info = self.api.users.get(user_ids=name, fields='bdate, sex, city, books, music, interests')
    return api

def prepare_to_search(user):
    """Функция проверяет, все ли обязательные поля заполненны, и просит ввести вручную, если данных нет"""
    try:
        birthday = datetime.strptime(user.bdate, "%d.%m.%Y")
        age = birthday.year
        age = datetime.now().year - age
    except Exception as er:
        print(er, ' - год рождения не указан')
        age = int(input('Введите возраст кандидата: '))
    user.age = age
    user.start_age = age - 5
    user.finish_age = age + 5

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
    lapssh = User('stupport', API)
    lapssh.get_mutual(4298081)
    print(lapssh.mutual_friends)

    #print(lapssh)
    prepare_to_search(lapssh)
    #test005 = User(4298081, API)  # Отавина
    #print(test005.age)
    #exit()
    res = lapssh.search_users()
    print(len(res))
    print(res)
    for id in res:
        id = User(id, API)
        id.get_mutual(lapssh.id)
        print(id.age, id.mutual_friends)
        time.sleep(0.4)

    # test005.search_users()


if __name__ == '__main__':
    main()
