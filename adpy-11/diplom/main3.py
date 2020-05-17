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
        self.groups_get()

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

    def groups_get(self):
        time.sleep(0.35)
        print('Получить группы пользователя ', self.id)
        try:
            self.groups = self.api.groups.get(user_id=self.id)['items']
            print('Получен список групп пользователя', self.id, ' ', len(self.groups))
        except Exception as err:
            print(err, ' - при попытке получить группы пользователя')
            self.groups = []

    def get_mutual(self, target):
        # target = int(target)
        time.sleep(0.4)
        try:
            self.mutual_friends = self.api.friends.getMutual(source_uid=self.id, target_uid=target)
        except Exception as err:
            print('Профиль ', self.id, ' закрыт, данные не получены')
            self.mutual_friends = False

    def calc_kpi(self, target):
        """Метод находит общее между пользователем и объектом исследования на основе следующей системы весов
        общий друг              10 баллов
        совпадение возраста     7 баллов
        общая группа            5 баллов
        совпадение по музыке    3 балла
        совпадение по книге     2 балла
        совпадение по интересам 1 балл
        """
        kpi = 0
        try:
            for friend in self.mutual_friends:
                kpi += 10
                print(self.id, ' начислено 10 баллов за общего другана - ', self.mutual_friends)
        except:
            pass  # нет друзей
        if self.age == target.age:
            kpi += 7
            print(self.id, ' начислено 7 баллов за совпадение по возрасту')
        # поиск общих групп
        for group in target.groups:
            if group in self.groups:
                kpi += 5
                print(self.id, ' начислено 5 баллов за общую группу - ', group)
        # поиск совпадений по музыке
        if self.music and target.music:
            pattern = self.music.split(',')
            for i in pattern:
                if len(i) > 2:
                    if i in target.music:
                        kpi += 3
                        print(self.id, ' начислено 3 балл за совпадение по музыке - ', i)

        # поиск совпадений по книгам
        if self.books and target.books:
            pattern = self.books.split(',')
            for i in pattern:
                if len(i) > 2:
                    if i in target.books:
                        kpi += 2
                        print(self.id, ' начислено 2 балла за совпадение по книгам - ', i)

        # поиск совпадений по интересам
        if self.interests and target.interests:
            pattern = self.interests.split(',')
            for i in pattern:
                if len(i) > 2:
                    if i in target.interests:
                        kpi += 1
                        print(self.id, ' начислен 1 балл за совпадение по интересам - ', i)
        self.kpi = kpi

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
                                           age_to=self.finish_age, status=[1], count=7)
        candidates_items = candidates['items']
        # print(candidates_items)
        candidates_ = list()
        for i in candidates_items:
            candidates_.append(i['id'])
            # print(candidates['id'], candidates['last_name'], ' ', candidates['first_name'])
        return candidates_


def get_token():
    pass


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
    user.start_age = age - 2
    user.finish_age = age + 2


def sort_by_kpi(users_list):
    kpi_dict = dict()
    for user in users_list:
        kpi_dict[user.id] = user.kpi
    kpi_for_sort = list(kpi_dict.items())
    kpi_for_sort.sort(key=lambda i: i[1])
    kpi_for_sort.reverse()
    return kpi_for_sort


def get_10_users(users_list):
    count = 0
    top_10_users = []
    for user in users_list:
        if count == 10:
            break
        top_10_users.append(user)
        count += 1
    return top_10_users


#
# def get_friends_by_id(api, id):
#     print(api.friends.get(user_id=id))

#
# def get_info_by_id(api, id):
#     # print(id)
#     user_info = api.users.get(user_ids=id, fields='bdate, sex, home_town, interests')
#     print(user_info)
#     print('пол', user_info[0]['sex'])
#     print('дата рождения: ', user_info[0]['bdate'])
#     print('Расположение: ', user_info[0]['home_town'])
#     print('Интересы: ', user_info[0]['interests'])
#
#     user_groups = api.groups.get(user_id=id)
#
#     print('Состоит в группах: ', user_groups['items'])


def main():
    TOKEN = get_token()
    API = auth()

    # test002 = User(test_id) #Куварин
    # test003 = User(1)
    # test004 = User(13323484) # Олег (Закрытый)

    # user_error = User('askdjfhaskdjfhsakd')
    lapssh = User('stupport', API)
    lapssh.get_mutual(13323484)
    print(lapssh.mutual_friends, '- общие друзья')

    # print(lapssh)
    prepare_to_search(lapssh)
    # test005 = User(4298081, API)  # Отавина
    # print(test005.age)
    # exit()
    res = lapssh.search_users()
    base_users = list()

    for id in res:
        id = User(id, API)
        id.get_mutual(lapssh.id)
        if id.mutual_friends != [] and id.mutual_friends != False:
            print(id.id, '- найден общий друг ', id.mutual_friends)
        id.calc_kpi(lapssh)
        base_users.append(id)
        time.sleep(0.4)
    print('В базу добавлено ', len(base_users), ' пользователей')
    # test005.search_users()

    sorted_users = sort_by_kpi(base_users)
    top_10 = get_10_users(sorted_users)
    print(top_10)


if __name__ == '__main__':
    main()
