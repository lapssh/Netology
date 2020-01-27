documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

def menu():
    print('========================================================================')
    print('=-------------------------------SkyNet---------------------------------=')
    print('========================================================================')
    print('=                                                                      =')
    print('=  p   -   people  - Найти человека по номеру документа                =')
    print('=  l   -   list    - Вывести список всех документов                    =')
    print('=  s   -   shelf   - Вывести номер полки по номеру документа           =')
    print('=  a   -   add     - Добавить новый документ                           =')


menu()