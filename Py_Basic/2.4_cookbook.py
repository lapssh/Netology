# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#                          Яйцо | 2 | шт
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
def read_recipes(filename):
    with open(filename, 'rt', encoding='utf-8') as f:
        cook_book = dict()


        while True:
            name_recipies = f.readline().strip()
            new_line = f.readline()
            ingredient_count = int(new_line.strip())
            if name_recipies not in cook_book.keys():
                cook_book[name_recipies] = []
            for i in range (ingredient_count):
                parsnig_line = f.readline().strip().split('|')
                cook_book[name_recipies].append(
                    {'ingredient_name' : parsnig_line[0].strip(),
                     'quantity': int(parsnig_line[1].strip()),
                     'measure' : parsnig_line[2].strip()
                     })
            #print(f.readline())
            if not f.readline():
                break

        return cook_book


cook_book = read_recipes('recipes.txt')
print(cook_book)
