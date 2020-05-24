import vk
from user_class import User
import private_settings
from datetime import datetime
import time
import operator
import json
import sql
import file_base


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
    """ Функция проверяет, указан ли возраст, и просит ввести вручную, если данных нет """
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


def get_city(user):
    """ Функция проверяет, указан ли город, и просит ввести вручную, если данных нет """
    print('Функция определения города вызвана')
    print(f'{user.city=}')
    while True:
        if user.city == False:
            city = input('Введите город проживания пользователя: ')
            list_of_cityes = user.api.database.getCities(country_id=1, q=city)
            if list_of_cityes['count'] == 0:
                print('Населенного пункта с таким наименованием несуществует. Попробуйте снова.')
                continue
            break
    print(list_of_cityes)
    last_city = list_of_cityes['count']
    if list_of_cityes['count'] > 21:
        last_city = 21
    for i in range(1, last_city):
        print(i, ' - ', list_of_cityes['items'][i])
    city_choise = int(input('Выберите ваш город: '))
    user.city = list_of_cityes['items'][city_choise - 1]
    print('Вы выбрали ', list_of_cityes['items'][city_choise - 1])


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


def show_results(flag_db):
    if flag_db:
        result = get_10_users_from_db()
    else:
        result = get_10_users_from_file()
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
                print('Подготовка файла к записи')
                print(type(result))
                print(result)
                save_result(result)
                print('Данные сохранены! Удачной встречи! Будте счастливы! Всего Вам доброго!')
                exit()
            elif user_asnwer == '':
                show_results(flag_db)
            else:
                print('Неправильный ввод! Повторите!')
    print('Пользователи в базе закончились, сохраняем оставшихся')
    print(result)
    save_result(result)
    print('Данные сохранены! Удачной встречи! Будте счастливы! Всего Вам доброго!')
    exit()


def get_10_users_from_db():
    """ получить 10 пользователей из БД """
    users = []
    for i in range(10):
        user_ = sql.get_one()
        if user_ == False:
            print('Данных не осталось. Работа c БД  завершена')
            break
        users.append(user_)
    return users


def get_10_users_from_file():
    """ получить 10 пользователей из файла """
    users = []
    with open('fdatabase.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        tmp_count = 0
        for line in text:
            if tmp_count == 10:
                break
            users.append(eval(line))
            tmp_count += 1
        del text[0:10]
        with open('fdatabase.txt', 'w', encoding='utf-8') as f:
            f.writelines(text)
        return users


def main():
    TOKEN = get_token()
    API = auth(TOKEN)
    lapssh = User('stupport', API)
    print(lapssh.groups_get())
    target_id = get_target(API)
    target = User(target_id, API)
    get_age(target)  # получаем возраст цели
    if not target.city:  # уточняем город цели
        get_city(target)
    base_users = get_match_users(target, API)  # получаем список найденных пользователей
    get_top3_photos(base_users, API)  # сопоставляем три фотограифи
    sorted_users = reversed(sorted(base_users, key=operator.attrgetter('kpi')))  # сортируем по весам
    # - - - П Р А В К И - - -
    if sql.get_db_status() == False:
        db = False  # проверка доступности БД
    else:
        db = True
        sql.delete_tables()  # удаляем старые таблицы
        sql.create_db(target.id)  # создаем новые таблицы
    for i in sorted_users:
        temp = i.show_result()
        # print(temp)
        temp_json = json.dumps(temp)
        if db:
            sql.add_user(i.id, i.kpi, temp_json)  # отправляем все, что нашли в БД
        else:
            file_base.add_user(i.id, i.kpi, temp_json)  # отправляем все, что нашли в файл

    show_results(db)  # выводим результат


if __name__ == '__main__':
    main()
