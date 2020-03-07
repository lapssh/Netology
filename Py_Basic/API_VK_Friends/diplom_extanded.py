# Diploma v 2.2
import requests
import time
import json
from pprint import pprint
import private_vk_settings

timeout_count = 0  # счетчик ошибок по таймату
closed_profile_count = 0  # счетчик закрытых профилей
closed_groups = 0  # счетчик закрытых групп
deleted_profile_count = 0  # счетчик удаленных или забаненных пользователей


def get_params():
    return dict(
        access_token=TOKEN,
        v='5.103'
    )


def check_id():
    """
    Функция проверяет введенных id на валидность, и возвращает id
    :return:
    """
    params = get_params()
    while True:
        id = input('Введите id жертвы: ')
        params['user_ids'] = id
        response = requests.get('https://api.vk.com/method/users.get', params)
        try:
            print('Найден пользователь:')
            print('Имя: ', response.json()['response'][0]['first_name'])
            print('Фамилия: ', response.json()['response'][0]['last_name'])
            return id
        except:
            print('По такому id пользователь не найден. Повторите ввод.')
            continue


def get_list_of_groups(id):
    """
    Функция возвращает список групп по id пользователя
    """
    global closed_profile_count
    global timeout_count
    global deleted_profile_count
    params = get_params()
    params['user_id'] = id
    params['extended'] = 1
    params['fields'] = 'members_count'
    try:
        response = requests.get('https://api.vk.com/method/groups.get', params)
        if 'error' in response.json():
            if response.json()['error']['error_code'] == 6:
                timeout_count += 1
                return 'timeout'

        return response.json()['response']['items']
    except:
        if response.json()['error']['error_code'] == 18:
            print(f'\nПользователь {id} удален или забанен')
            deleted_profile_count += 1
        elif response.json()['error']['error_code'] == 7:
            print('\nУ пользователя с id', id, 'закрытый профиль, пропускаем....')
            closed_profile_count += 1
        elif response.json()['error']['error_code'] == 30:
            print('\nУ пользователя с id', id, 'закрытый профиль. Получить данные не возможно')
        else:
            print('\nПоймал неучтенную ошибку:')
            print(response.json())

        return []


def get_friens_by_id(id):
    """
    Функция возвращает список друзей по id
    """
    params = get_params()
    params['user_ids'] = id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']


def create_set_of_grups(id):
    global closed_groups
    get_params()
    friends_victim = get_friens_by_id(id)
    for friend in friends_victim:
        try:
            friend_groups = get_list_of_groups(friend)
            if friend_groups == 'timeout':
                time.sleep(0.35)
                friend_groups = get_list_of_groups(friend)
                continue
            if friend_groups == False:
                continue
        except:
            print('\nВозникло исключение на пользователе', friend)

        time.sleep(0.35)
        decore_counter = 0
        for group in friend_groups:
            try:
                if decore_counter > 60:
                    decore_counter = 0
                    print()
                group_name = group['name']
                group_id = group['id']
                group_members_count = group['members_count']
                set_of_groups.add((group_id, group_name, group_members_count))
                print('*', end='')
                decore_counter += 1
            except TypeError:
                print('Закрытый профиль, попробуйте снова. ')
                continue
            except:
                print('\n', group_name, '- Закрытая группа, данные не предоставлены.')
                closed_groups += 1
                decore_counter = 0
    return set_of_groups


# TASK: Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
if __name__ == '__main__':
    while True:
        user_token = input('Укажите токен доступа (ENTER) - для токена по умолчанию: ')
        if user_token == '':
            TOKEN = private_vk_settings.victim_token
        else:
            TOKEN = user_token
        params = get_params()
        response = requests.get('https://api.vk.com/method/users.get', params)
        try:
            if response.json()['error']['error_code'] == 5:
                print('Указан нерабочий токен, повторите ввод.')
                continue
        except:
            print('Токен рабочий')
        print(response.json())

        break

    set_of_groups = set()
    name_gid_members_count = dict()

    ID = check_id()

    friends_victim = get_friens_by_id(ID)
    victim_groups = get_list_of_groups(ID)
    set_of_victim = set()
    for group in victim_groups:
        group_name = group['name']
        group_id = group['id']
        try:
            group_members_count = group['members_count']
        except:
            print('\nГруппа забанена', group)
        set_of_victim.add((group_id, group_name, group_members_count))
    if victim_groups != []:
        set_of_groups = create_set_of_grups(id)
    print('\nСообщества жертвы:')
    print(set_of_victim)
    print()
    diff_groups = set_of_victim - set_of_groups
    print('Отличия: ')
    js_data = []
    for i in diff_groups:
        elem = {
            "name": i[1],
            "gid": i[0],
            "members_count": i[2]
        }
        js_data.append(elem)
    pprint(diff_groups)
    with open('groups.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(js_data, ensure_ascii=False))
    print('\nОшибок по таймауту: ', timeout_count)
    print('Закрытых профилей: ', closed_profile_count)
    print('Закрытых групп: ', closed_groups)
    print(('Удаленных (забаненных пользователей):'), deleted_profile_count)
    print('\nДанные сохранены в файле "groups.json"')
