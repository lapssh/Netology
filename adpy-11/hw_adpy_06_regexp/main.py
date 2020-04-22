# TODO  Починить адресную книгу, используя регулярные выражения.
# TODO  Структура данных будет всегда:  lastname,firstname,surname,organization,position,phone,email
# TODO  Допустимый формат телефонных номеров: +7(999)999-99-99, а с добавочным +7(999)999-99-99 доб.9999
import csv
from pprint import pprint
import re


def import_data(file='phonebook_raw.csv'):
    """Из CSV-файла имортируем сырые данные, удаляем заголовок и возвращаем список строк    """
    with open(file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list

def merge_duplicate(base_humans):
    """Удаляем дубликаты"""

    base_humans2 = []
    while len(base_humans) >= 2:
        tmp_user = base_humans[0]
        print('tmp = ', tmp_user.lastname)
        base_humans.pop(0)
        print('вырезал первого')
        for user in base_humans:
            print(tmp_user.lastname, ' равен ли ', user.lastname)
            if tmp_user.lastname == user.lastname:
                print('парняги говорят что да')
                tmp_user.firstname = user.firstname
                tmp_user.surname = user.surname
                tmp_user.company = user.company
                tmp_user.position = user.position
                tmp_user.tel_number = user.tel_number
                tmp_user.email = user.email
                for i in base_humans2:
                    if tmp_user.lastname == i.lastname:
                        pass
                    else:
                        base_humans2.append(tmp_user)

                # print('парняги говорят - НЕТ')
                # base_humans2.append(user)
    return base_humans2


    # for id, user in enumerate(base_humans):
    #     for user2 in enumerate(base_humans)+1:
    #         if user.lastname == user2.lastname and user.firstname == user2.firstname:
    #             print('Найден дубль для ', user.lastname, user.firstname)
    #             print(user.tel_number, user2.tel_number)
    #             if user.tel_number == '':
    #                 user.tel_number = user2.tel_number
    #             if user.company == '':
    #                 user.company = user2.company
    #                 print(user.company, 'добавили!')
    #             if user.position == '':
    #                 user.position = user2.position
    #                 print('добавил должность', user.position)
    #             if user.email == '':
    #                 user.email = user2.email
    #             if user.surname == '':
    #                 try:
    #                     user.surname = user2.surname
    #                 except:
    #                     pass # отчество отсутствует в обоих запясях
    #             base_humans_without_double.append(user)
    #         user2_index += 1
    # return base_humans_without_double






if __name__ == '__main__':

    # TODO 1: выполните пункты 1-3 ДЗ
    contacts_list = import_data()


    # pprint(contacts_list)

    class Human:
        def __init__(self, data):
            self.data = data



        def find_email(self):
            self.email = self.data[6]
            return self.email

        def find_phone(self):
            self.tel_number = self.data[5]
            pattern_1 = re.compile(r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})')
            pattern_2 = re.compile(r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2}).*?(\d{4)')
            self.tel_number = re.sub(pattern_1, '+7(\\2)\\3-\\4-\\5', self.tel_number)
            self.tel_number = re.sub(pattern_2,'+7(\\2)\\3-\\4-\\5 доб.\\6', self.tel_number)
            return self.tel_number

        def find_position(self):
            self.position = self.data[4]
            return self.position

        def find_company(self):
            self.company = self.data[3]
            return self.company

        def find_name(self):
            self.full_name = self.data[0] +' '+ self.data[1] + ' ' + self.data[2]
            self.full_name = self.full_name.split()
            self.lastname = self.full_name[0]
            try:
                self.firstname = self.full_name[1]
                self.surname = self.full_name[2]
            except:
                self.surname = ''
                # если отсутствует отчество
            # if len(self.full_name) == 2:
            #     self.firstname = self.full_name[1]
            #     print('длинна равна имени для ', self.firstname)
            #     if len(self.full_name) == 3:
            #         self.surname = self.full_name[2]
            return self.full_name

        def show_base(self):
            try:
                print('-' * 40)
                print('Фамилия: \t',self.lastname,'\nИмя: \t\t', self.firstname, '\nОтчество: \t', self.surname)
                print('Организация:', self.company)
                print('Должность:\t', self.position)
                print('Телефон:\t', self.tel_number)
                print('e-mail:\t\t', self.email)
            except:
                print('Фамилия: \t',self.lastname,'\nИмя: \t\t', self.firstname) # отсутствует отчество
                print('Организация:', self.company)
                print('Должность:\t', self.position)
                print('Телефон:\t', self.tel_number)
                print('e-mail:\t\t', self.email)



    base_humans = list()
    for homo in contacts_list:
        base_humans.append(Human(homo))
    for i in base_humans:
        i.find_email()
        i.find_phone()
        i.find_position()
        i.find_company()
        i.find_name()

    for i in base_humans:
        i.show_base()

    #base_humans_without_doubles = merge_duplicate(base_humans)
    base_humans.pop(0)
    print()
    print()
    print('БЕЗ ДУБЛИКАТОВ')
    base_humans2 = merge_duplicate(base_humans)
    for i in base_humans2:
         i.show_base()


    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_list)
