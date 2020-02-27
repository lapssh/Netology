import requests
import json
import private_vk_settings

# TASK: Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
#token = private_vk_settings.diplom_token
token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
victim = 'https://vk.com/eshmargunov'
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
    response = requests.get('https://api.vk.com/method/groups.get', params)
    #params['count'] = 1000

    return  response.json()

def get_friens_by_id(id):
    """
    Функция возвращает список друзей по id
    """
    params = get_params()
    print(id)
    params['user_ids'] = id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()

id = '392307838'
id_shmargunov = '171691064'
friends_victim = get_friens_by_id(id_shmargunov)
print('Друзья жертвы: ', friends_victim['response']['items'])
victim_groups = get_list_of_groups(id_shmargunov)
#print('Жертва состоит в следующих группах: ', victim_groups['response']['items'])
for group in victim_groups['response']['items']:
    group_name = group['name']
    group_id = group['id']
    print('Наша жертва состоит в группе - "', group_name, '" c id ="', group_id,'"')

