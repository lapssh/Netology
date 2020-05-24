from datetime import datetime
import time


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
        books, music, interests, photo_max, home_town')
        # self.home_town = self.user_info[0]['home_town']
        # if 'home_town' not in self.user_info[0]:
        #     self.home_town = False
        # else:
        #     self.home_town = self.user_info[0]['home_town']
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
        общий город             9 баллов
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

        # проверка совпадения города
        if self.city == target.city:
            kpi += 9
            self.common += (('начислено 9 баллов за совпадение города' + '\n'))

        # проверка совпадения по возрасту
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
                                               age_to=self.finish_age, status=[1], count=15)
        else:
            candidates = self.api.users.search(sex=sex_, age_from=self.start_age,
                                               age_to=self.finish_age, status=[1], count=15)
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
