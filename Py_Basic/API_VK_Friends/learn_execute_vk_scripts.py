import private_vk_settings
import requests
import traceback

#token = private_vk_settings.diplom_token
token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
#id = private_vk_settings.user_id
id = '171691064'
#kod = 'var friends=API.friends.get({fields : "count"}); return friends;'
#kod = 'var friends=API.friends.get().count; return friends;'
#kod = 'var friends=API.users.get({user_ids:1}); var test=friends@.first_name[0]; return test;'
#kod = "var friends=API.friends.get(); var test=friends; return test;"
#kod = "var count=API.friends.get().count; return count;" #  Рабочий вариант получения счетчика друзей
#kod = "var friends=API.friends.get().items; return friends;" # Рабочий вариант получения списка друзей
#kod = "var friends=API.friends.get().items; var count=API.friends.get().count; var index=0; while (index < friends.length){ТУТ ДЕРГАЕМ МЕТОД ГРУППЫ;};return friends;"
#kod = "var groups=API.groups.get();return groups;" # Рабочий вариант получения списка групп
#kod = "var groups=API.groups.get().items; return groups;"
with open('vk_script.vks') as f:
    kod = f.read()

params = {
    'access_token': token,
    'v': '5.103',
    'code': kod
}
# response = requests.get('https://api.vk.com/method/friends.get', params)
# 'extended': 1,
# 'fields': 'members_count',
try:
    response = requests.get('https://api.vk.com/method/execute' , params)
    print(response.json())
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    print('какая то шляпка')
