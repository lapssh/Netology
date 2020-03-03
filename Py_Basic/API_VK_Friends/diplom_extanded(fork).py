import requests
import time
import json
from pprint import pprint
import private_vk_settings
import traceback


def get_params():
    return dict(
        access_token=token,
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
            # if response.json()['response'][0]['is_closed'] == True:
            #     print('У пользователя профиль закрыт, получить данные не возможно, попробуйте с другим id.')
            #     continue
            print('Найден пользователь:')
            print('Имя: ', response.json()['response'][0]['first_name'])
            print('Фамилия: ', response.json()['response'][0]['last_name'])
            print(response.json())

            return id
        except:
            print('По такому id пользователь не найден. Повторите ввод.')
            continue


def get_list_of_groups(id):
    """
    Функция возвращает список групп по id пользователя
    """
    params = get_params()
    params['user_id'] = id
    params['extended'] = 1
    params['fields'] = 'members_count'
    try:
        response = requests.get('https://api.vk.com/method/groups.get', params)
        return response.json()['response']['items']
    except:
        print('\nУ пользователя с id', id, 'закрытый профиль, пропускаем....')

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
    get_params()
    friends_victim = get_friens_by_id(id)
    for friend in friends_victim:
        try:
            friend_groups = get_list_of_groups(friend)
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
                decore_counter = 0
    return set_of_groups


# TASK: Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
if __name__ == '__main__':
    # token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    token = private_vk_settings.victim_token
    # token = private_vk_settings.diplom_token
    # victim = 'https://vk.com/eshmargunov' 171691064
    # ceridan 229346
    # onega 267357
    # id_shmargunov = '171691064'
    set_of_groups = set()
    name_gid_members_count = dict()

    # id_shmargunov = '171691064'

    id = check_id()

    friends_victim = get_friens_by_id(id)
    victim_groups = get_list_of_groups(id)
    print(victim_groups)
    set_of_victim = set()
    for group in victim_groups:
        group_name = group['name']
        group_id = group['id']
        group_members_count = group['members_count']
        set_of_victim.add((group_id, group_name, group_members_count))
    if victim_groups != []:
        set_of_groups = create_set_of_grups(id)
    print('\nВсе сообщества:')
    print(set_of_groups)
    print()
    print('Сообщества жертвы:')
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
    print('\nДанные сохранены в файле "groups.json"')
