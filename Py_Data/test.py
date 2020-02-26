stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]
uniq_user_count = 0
view_count = 0
user_name = ''
for i in stream:
    s = i.split(',')
    view_count += int(s[2])
    if user_name != s[1]:
        uniq_user_count += 1
        user_name = s[1]
print(uniq_user_count, view_count,  view_count / uniq_user_count)

# avg_user_view = {}
# count_view = 0
# for i in stream:
#     s = i.split(',')
#     if s[1] not in avg_user_view:
#         avg_user_view[s[1]] = int(s[2])
#         count_view += 1
#         continue
#     avg_user_view[s[1]] += int(s[2])
#     count_view += 1
# print(avg_user_view)

#     while i[2]
# count_uniq = dict()
# for user in list_stream:
#     if user[1] not in count_uniq:
#         count_uniq[user[1]] = [int(user[2]), 1]
#     else:
#         count_uniq[user[1]][0] += int(user[2])
#         count_uniq[user[1]][1] += 1
# for user, value in count_uniq.items():
#     print(f'У пользователя {user} было в среднем {value[0]/value[1]} просмотров.')