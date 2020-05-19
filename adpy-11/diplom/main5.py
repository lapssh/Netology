import vk
import private_settings
from datetime import datetime
import time
import operator
import json
import sql


class User():
    """Клас описывает основные параметры пользователя, которые будем сохранять в базу"""

    def __init__(self, name, api):
        self.start_age = None
        self.finish_age = None
        self.top3 = None
        self.api = api
        self.name = name
        self.common = ''
        self.get_data()
        self.groups_get()

    def get_data(self):
        self.user_info = self.api.users.get(user_ids=self.name, fields='bdate, sex, city, \
        books, music, interests, photo_max')
        self.id = self.user_info[0]['id']
        self.sex = self.user_info[0]['sex']
        self.photo_max = self.user_info[0]['photo_max']
        if 'city' not in self.user_info[0]:
            self.city = False
        else:
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

    def groups_get(self):
        time.sleep(0.33)
        print('Получить группы пользователя ', self.id)
        try:
            self.groups = self.api.groups.get(user_id=self.id)['items']
            print('Получен список групп пользователя', self.id, ' ', len(self.groups))
        except Exception as err:
            self.groups = []
        return self.groups

    def get_mutual(self, target):
        time.sleep(0.33)
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
                self.common += ('начислено 10 баллов за общего другана - ' + str(self.mutual_friends) + '\n')
        except:
            pass  # нет друзей
        if self.age == target.age:
            kpi += 7
            self.common += ('начислено 7 баллов за совпадение по возрасту' + '\n')
        # поиск общих групп
        for group in target.groups:
            if group in self.groups:
                kpi += 5
                self.common += (' начислено 5 баллов за общую группу - ' + str(group) + '\n')
        # поиск совпадений по музыке
        if self.music and target.music:
            pattern = self.music.split(',')
            for i in pattern:
                if len(i) > 2:
                    if i in target.music:
                        kpi += 3
                        self.common += ('начислено 3 балла за совпадение по музыке - ' + i + '\n')

        # поиск совпадений по книгам
        if self.books and target.books:
            pattern = self.books.split(',')
            for i in pattern:
                if len(i) > 2:
                    if i in target.books:
                        kpi += 2
                        self.common += (' начислено 2 балла за совпадение по книгам - ' + i + '\n')

        # поиск совпадений по интересам
        if self.interests and target.interests:
            pattern = self.interests.split(',')
            for i in pattern:
                if len(i) > 2:
                    if i in target.interests:
                        kpi += 1
                        self.common += ('начислен 1 балл за совпадение по интересам - ' + i + '\n')
        self.kpi = kpi
        self.common += ('-' * 20 + '\nВсего совпадений на ' + str(kpi) + ' баллов.')

    def info(self, api):
        """ Метод возвращает массив данных о юзере"""
        user = api.users.get(user_id=self.id)
        return user[0]

    def search_users(self):
        """ Метод получает список пользователей подходящих под базовый запрос (город, диапазон возраста, статус, пол) """
        if self.sex == 1:
            sex_ = 2
        else:
            sex_ = 1
        if self.city:
            candidates = self.api.users.search(city=self.city['id'], sex=sex_, age_from=self.start_age,
                                               age_to=self.finish_age, status=[1], count=50)
        else:
            candidates = self.api.users.search(sex=sex_, age_from=self.start_age,
                                               age_to=self.finish_age, status=[1], count=50)
        candidates_items = candidates['items']
        candidates_ = list()
        for i in candidates_items:
            candidates_.append(i['id'])
        return candidates_

    def show_result(self):
        tmp_list = []
        self.url = ('https://vk.com/id' + str(self.id))
        try:
            for i in self.top3:
                s = i['sizes']
                for j in s:
                    if j['type'] == 'x':
                        tmp_list.append(j['url'])

        except:
            tmp_list.append('Профиль закрыт, есть только фото профиля')
            tmp_list.append(self.photo_max)
        answer = dict()
        answer['id'] = str(self.id)
        answer['url'] = str(self.url)
        answer['photos'] = tmp_list
        self.answer = answer
        return answer


def get_token():
    token = input('Введите Ваш ТОКЕН: ')
    return token


def auth(TOKEN):
    """ авторизация в ВК """
    try:
        session = vk.Session(access_token=TOKEN)
        api = vk.API(session, v='5.103', lang='ru', timeout=10)
        test = api.users.get()
        print('Введенный токен корректен - ', TOKEN)
    except:
        session = vk.Session(access_token=private_settings.TOKEN)
        api = vk.API(session, v='5.103', lang='ru', timeout=10)
        print('Введенный токен не подошёл, исопльзую по-умолчанию')
    return api


def get_target(api):
    """ Функция запрашивает id или screen_name пользователя """
    while True:
        try:
            id_or_name = input('Введите ID или Screen Name пользователя: ')
            test = api.users.get(user_ids=id_or_name)
            print('Ползователь найден!')
            print(test)
            return id_or_name
        except:
            print('Пользователь незарегистрирован, повторите ввод!')


def get_age(user):
    """Функция проверяет, указан ли возраст, и просит ввести вручную, если данных нет"""
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


def get_match_users(target, api):
    res = target.search_users()
    base_users = list()

    for id in res:
        id = User(id, api)
        id.get_mutual(target.id)
        if id.mutual_friends != [] and id.mutual_friends != False:
            print(id.id, '- найден общий друг ', id.mutual_friends)
        id.calc_kpi(target)
        base_users.append(id)
        time.sleep(0.4)
    print('В базу добавлено ', len(base_users), ' пользователей')
    return base_users


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


def get_top3_photos(users, api):
    for user in users:
        time.sleep(0.33)
        try:
            result = api.photos.get(user_id=user.id, album_id='profile', extended=1)
        except Exception as err:
            result = False

        if result:
            result = result['items']
            top3 = find_top3(result)
            user.top3 = top3
        else:
            user.top3 = 'Профиль закрыт, фото не получены'
    return users


def find_top3(list):
    photos_sorted = sorted(list, key=lambda x: x['likes']['count'])
    top3_photos = photos_sorted[len(photos_sorted) - 3:len(photos_sorted)]
    return top3_photos


def save_result(data):
    with open('top_10_users_with_photo.json', 'w', encoding='utf-8') as f:
        data_ = json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
        f.write(data_)
    print('Запись результатов в файл завершена.')


def show_results():
    result = get_10_users_from_db()
    while len(result) == 10:
        for user in result:
            print(user)
        while True:
            user_asnwer = input('e[X]it: Выход      '
                                '[S]ave: Сохранить в файл       '
                                'ENTER: Показать следующих 10 пользователей: ')
            if user_asnwer in ['X', 'x', 'exit', 'e[X]it', 'EXIT']:
                print('Заверешение работы программы. Удачной встречи! Будте счастливы! Всего Вам доброго!')
                exit()
            elif user_asnwer in ['s', 'S', 'Save', 'SAVE', 'save', '[S]ave']:
                save_result(result)
                print('Данные сохранены! Удачной встречи! Будте счастливы! Всего Вам доброго!')
                exit()
            elif user_asnwer == '':
                show_results()
            else:
                print('Неправильный ввод! Повторите!')
    print('до новых встреч')
    exit()


def get_10_users_from_db():
    users = []
    for i in range(10):
        user_ = sql.get_one()
        if user_ == False:
            print('Данных не осталось. Работа c БД  завершена')
            break
        users.append(user_)
    return users


def main():
    TOKEN = get_token()
    API = auth(TOKEN)
    lapssh = User('stupport', API)
    print(lapssh.groups_get())
    target_id = get_target(API)
    target = User(target_id, API)
    get_age(target)  # получаем возраст цели
    base_users = get_match_users(target, API)  # получаем список найденных пользователей
    get_top3_photos(base_users, API)  # сопоставляем три фотограифи
    sorted_users = reversed(sorted(base_users, key=operator.attrgetter('kpi')))  # сортируем по весам
    sql.delete_tables()  # удаляем старые таблицы
    sql.create_db(target.id)  # создаем новые таблицы
    for i in sorted_users:
        temp = i.show_result()
        print(temp)
        temp_json = json.dumps(temp)
        sql.add_user(i.id, i.kpi, temp_json)  # отправляем все, что нашли в БД

    show_results()  # выводим результат


if __name__ == '__main__':
    main()
