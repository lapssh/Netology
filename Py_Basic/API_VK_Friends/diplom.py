import requests
import time
import json
import private_vk_settings

# TASK: Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
#token = private_vk_settings.diplom_token
token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
victim = 'https://vk.com/eshmargunov'
set_of_groups = set()
name_gid_members_count = dict()
params = {
    'access_token': token,
    'v': '5.103'
}


def get_params():
    return dict(
        access_token=token,
        v='5.103'
    )
def get_list_of_groups(id):
    """
    Функция возвращает список групп по id пользователя
    """
    params = get_params()
    params['user_id'] = id
    params['extended'] = 1
    try:
        response = requests.get('https://api.vk.com/method/groups.get', params)
        #params['count'] = 1000

        return  response.json()['response']['items']
    except:
        print('Тут что-то пошло не так, давайте разбираться')
        print('response: ', response.text)
        print('У пользователя с id', id, 'закрытый профиль, пропускаем....')
        return False


def get_friens_by_id(id):
    """
    Функция возвращает список друзей по id
    """
    params = get_params()
    print(id)
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
            print('Возникло исключение на пользователе', friend)
        time.sleep(0.5)
        for group in friend_groups:
            group_name = group['name']
            group_id = group['id']
            print(group_id, group_name)
            set_of_groups.add((group_id,group_name))
    return set_of_groups




id = '392307838'
id_shmargunov = '171691064'
friends_victim = get_friens_by_id(id_shmargunov)
print('Друзья жертвы: ', friends_victim)
victim_groups = get_list_of_groups(id_shmargunov)
#print('Жертва состоит в следующих группах: ', victim_groups['response']['items'])
for group in victim_groups:
    group_name = group['name']
    group_id = group['id']
    print('Наша жертва состоит в группе - "', group_name, '" c id ="', group_id,'"')
create_set_of_grups(id_shmargunov)
print(set_of_groups)