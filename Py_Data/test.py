random_list = ['2018-01-01', 'yandex', 'cpc', 100,6,5,4,'12']
deep_dict = {}
deep_dict[random_list[-2]] = random_list[-1]
random_list.pop()
random_list.pop()
new_dict = {}
for i in reversed(random_list):
    new_dict = {i : deep_dict}
    deep_dict = new_dict
print(new_dict)