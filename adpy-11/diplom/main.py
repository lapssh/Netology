# импорт модуля вк
# import vk_api
import vk
import private_settings


class User():
    """VK User"""

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.id = ''

    # аторизирует юзера
    def auth(self):
        session = vk.AuthSession(app_id='5340228', user_login=self.login, user_password=self.password)
        api = vk.API(session)
        return api

    # возвращает массив объектов друзей
    def friends(self, api):
        # возвращает в том порядке, в котором расположены в разделе Мои
        user_friends = api.friends.get(user_id=self.id, order='hints')
        return user_friends

    # возвращает количество друзей
    def friends_count(self, api):
        user_friends = User.friends(self, api)
        friends_count = len(user_friends)
        return friends_count

    # возвращает массив данных о юзере
    def info(self, api):
        user = api.users.get(user_id=self.id)
        return user[0]



def get_friends_by_id(api, id):
    print(api.friends.get(user_id=id))

def get_info_by_id(api, id):
    #print(id)
    user_info = api.users.get(user_ids=id, fields='bdate, sex, home_town, interests')
    print(user_info)
    print('пол', user_info[0]['sex'])
    print('дата рождения: ', user_info[0]['bdate'])
    print('Расположение: ', user_info[0]['home_town'])
    print('Интересы: ', user_info[0]['interests'])

    user_groups = api.groups.get(user_id=id)

    print('Состоит в группах: ', user_groups['items'])


def main():
    session = vk.Session(access_token=private_settings.TOKEN)
    api = vk.API(session, v='5.103', lang='ru', timeout=10)
    #get_friends_by_id(api, 636197)
    test_id = 636197
    get_info_by_id(api, test_id)



if __name__ == '__main__':
    main()
