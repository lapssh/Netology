import csv

flats_list = list()

with open('output.csv', encoding='utf-8', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


# TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
# и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
new_building_count = 0
for flat in flats_list:
    if "новостройка" in flat:
        #        print("{}".format(flat)) # Код, который был
        print(flat[0])
        new_building_count += 1
# 2) добавьте в код подсчет количества новостроек
print(f'Колличество новостроек в списке: {new_building_count}')


# TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID,
# Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
flat_info = {"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]}
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был
# не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1
subway_dict = {}
description_dict = {}
for flat in flats_list:
    description_dict[flat[0]] = 'rooms: ' + str(flat[1]), 'type: ' + str(flat[2]), 'price: ' + str(flat[11])
    subway = flat[3].replace("м.", "")
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
#    subway_dict[subway].append(flat[0]) # БЫЛО
    subway_dict[subway].append(description_dict[flat[0]])  # СТАЛО

#print(subway_dict)
# for i in description_dict:
#     print(i, description_dict[i])

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
for i in subway_dict:
    print(i)
    print('Колличество квартир на раёне: ', len(subway_dict[i]))
    print(subway_dict[i])