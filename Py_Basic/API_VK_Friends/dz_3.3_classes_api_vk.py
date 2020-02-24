import private_vk_settings
import requests

TOKEN = private_vk_settings.access_token
params = {
    'access_token': TOKEN,
    'v': '5.95'
}


class User:
    def __init__(self, token, user_id, first_name=None, last_name=None):
        self.token = token
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.get_name_from_id(user_id)

    def __and__(self, target):
        # возможность найти общих друзей через оператор &
        self_friends_list = set(self.friend_list)
        target_friends_list = set(target.friend_list)
        mutual_friends_list = self_friends_list.intersection(target_friends_list)
        mutual_list = list(mutual_friends_list)
        list_of_mutual_friends = list()
        for vk_user in mutual_list:
            new_user = User(TOKEN, vk_user)
            list_of_mutual_friends.append(new_user)
        return list_of_mutual_friends

    def __str__(self):
        # Вывод ссылки на профиль пользователя
        profile_link = f'https://vk.com/id{self.id}'
        return profile_link

    def get_params(self):
        return dict(
            access_token=self.token,
            v='5.103'
        )

    def get_name_from_id(self, user_id):
        params['user_ids'] = user_id
        response = requests.get('https://api.vk.com/method/users.get', params=params)
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']
        self.id = response.json()['response'][0]['id']
        return response.json()

    def friends_get(self):
        """
        При вызове сохраняет список id друзей в переменной self.friend_list
        """
        params = self.get_params()
        params['user_id'] = self.id
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        self.friend_list = response.json()['response']['items']
        return response.json()['response']['items']

    def friends_getMutual(self, source_uid, target_uid):
        """
        Функция сделана для проверки результата средствами API самой VK
        """
        params = {
            'access_token': self.token,
            'v': '5.95',
            'source_uid': source_uid,
            'target_uid': target_uid
        }
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        return response.json()

    def print_user_info(self):
        """
        Вывод данных экземпляра пользователя ВК (для диагностики)
        """
        print('=' * 60)
        print(f'Данные по пользователю с {self.id=}')
        print(f'{self.first_name=}')
        print(f'{self.last_name=}')
        print(f'Список id друзей: {self.friends_get()}')
        print('=' * 60)
        return


alexey = User(TOKEN, '392307838')
pletenkin = User(TOKEN, '267357')
mero = User(TOKEN, '13323484')

alexey.print_user_info()
print(alexey.friend_list)
mero.print_user_info()
my_test_list = alexey & mero
print(my_test_list[0].first_name)
print(alexey)
