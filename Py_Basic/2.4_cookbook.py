def read_recipes(filename):
    with open(filename, 'rt', encoding='utf-8') as f:
        cook_book = dict()
        while True:
            name_recipies = f.readline().strip()
            new_line = f.readline()
            ingredient_count = int(new_line.strip())
            if name_recipies not in cook_book.keys():
                cook_book[name_recipies] = []
            for i in range(ingredient_count):
                parsnig_line = f.readline().strip().split('|')
                cook_book[name_recipies].append(
                    {'ingredient_name': parsnig_line[0].strip(),
                     'quantity': int(parsnig_line[1].strip()),
                     'measure': parsnig_line[2].strip()
                     })
            if not f.readline():
                break
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish in dishes:
        ingreds = cook_book[dish]
        for i in ingreds:
            if i['ingredient_name'] not in shop_list:
                shop_list[i['ingredient_name']] = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
            else:
                total = shop_list[i['ingredient_name']]['quantity']
                shop_list[i['ingredient_name']] = {'measure': i['measure'],
                                                   'quantity': i['quantity'] * person_count + total}
    return shop_list


def output_for_humans(shop_list, person_count):
    print(f'Мы пригласили на ужин {person_count} человек.')
    print('А значит нам пора отправлятся за покупками.')
    print('Что бы приготовить наши блюда нам потребуется:')
    for ingr, value in shop_list.items():
        print(f'{ingr} в колличестве {value["quantity"]} {value["measure"]}')


cook_book = read_recipes('recipes.txt')
dishes = ['Запеченный картофель', 'Омлет']
# person_count = int(input('Введите количество персон: '))
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
output_for_humans(shop_list, person_count)
