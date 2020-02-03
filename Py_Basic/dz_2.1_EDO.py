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
    print('=  p   -   people  - Найти человека по номеру документа                =')
    print('=  l   -   list    - Вывести список всех документов                    =')
    print('=  s   -   shelf   - Вывести номер полки по номеру документа           =')
    print('=  a   -   add     - Добавить новый документ                           =')
    print('=  q   -   quit    - Завершить работу                                  =')
    print('========================================================================')

def find_people_by_doc():
    while True:
        doc_number = input('Введите номер документа: ')
        for document in documents:
            if document['number'] == doc_number:
                return ('Под номером документа в системе зарегистрирован ', document['name'])

        return('ВНИМАНИЕ!! Человек с таким номером документа не зарегистрирован в системе.')
def list_all_docs():
       #print('========================================================================')
    for document in documents:
        print('Тип документа: ' + document['type'] + '  Номер: ' + document['number'] + '  Имя: ' + document['name'])
    input('Для продолжения нажмите ENTER')

def dir_by_the_number():
    '''
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    :return:
    '''
    while True:
        num_doc = input('Введите номер документа:')
        print(directories.values())
        for i in directories.values():
            for j in i:
                print(f'j и i    {j}   {i}')
                if num_doc == j:
                    my_val = i
        print('Нужный мне список: ', my_val)

        for k,v in directories.items():
            if v == my_val:
                dir = k
        print('Все добро лежит на ' + k + '-й полке')

                #print(directories.get(i))
        # #directories.values() :
        #     print('В архиве отсутствует документ под таким номером')
        #     print('q - Выйти в меню, ENTER - повторить поиск')
        #     user_click = input().lower()
        #     if user_click == 'q':
        #         break
        # else:
        #     print('Документ № ' + str(num_doc) + ' хранится на ' + directories.keys() + 'полке')



def menu_click():
    while True:
        correct_click = ['p', 'l', 's', 'a', 'q']
        click = input('Выберите действие:').lower()
        if click not in correct_click:
            print('Ошибка ввода, повторите ввод: ')
            continue
        else:
            return click

while True:
    menu()
    click = menu_click()
    if click == 'p':
        print(find_people_by_doc())
    elif click =='q':
        print('Работа программы завершена. Хорошего дня!')
        break
    elif click == 'l':
        list_all_docs()
    elif click == 's':
        dir_by_the_number()

