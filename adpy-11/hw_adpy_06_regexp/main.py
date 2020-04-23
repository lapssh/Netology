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
    while base_humans != []:
        tmp_user = base_humans[0]
        base_humans.pop(0)
        for user in base_humans:
            if tmp_user.lastname == user.lastname and tmp_user.firstname == user.firstname:
                if tmp_user.surname == '':
                    tmp_user.surname = user.surname
                if tmp_user.company == '':
                    tmp_user.company = user.company
                if tmp_user.position == '':
                    tmp_user.position = user.position
                if tmp_user.tel_number == '':
                    tmp_user.tel_number = user.tel_number
                if tmp_user.email == '':
                    tmp_user.email = user.email
        else:
            for i in base_humans2:
                if i.lastname == tmp_user.lastname:
                    break
            else:
                base_humans2.append(tmp_user)
    return base_humans2


def make_new_contact_list(base_humans):
    new_contact_list = []
    new_contact_list.append('lastname,firstname,surname,organization,position,phone,email\n')
    for i in base_humans:
        row = i.lastname + ',' + i.firstname + ',' + i.surname + ',' + i.company + ',' + (
                i.position + ',' + i.tel_number + ',' + i.email + '\n'
        )
        new_contact_list.append(row)
    return new_contact_list


if __name__ == '__main__':

    # TODO 1: выполните пункты 1-3 ДЗ
    contacts_list = import_data()


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
            self.tel_number = re.sub(pattern_2, '+7(\\2)\\3-\\4-\\5 доб.\\6', self.tel_number)
            return self.tel_number

        def find_position(self):
            self.position = self.data[4]
            return self.position

        def find_company(self):
            self.company = self.data[3]
            return self.company

        def find_name(self):
            self.full_name = self.data[0] + ' ' + self.data[1] + ' ' + self.data[2]
            self.full_name = self.full_name.split()
            self.lastname = self.full_name[0]
            try:
                self.firstname = self.full_name[1]
                self.surname = self.full_name[2]
            except:
                self.surname = ''
            return self.full_name

        def show_base(self):
            try:
                print('-' * 40)
                print('Фамилия: \t', self.lastname, '\nИмя: \t\t', self.firstname, '\nОтчество: \t', self.surname)
                print('Организация:', self.company)
                print('Должность:\t', self.position)
                print('Телефон:\t', self.tel_number)
                print('e-mail:\t\t', self.email)
            except:
                print('Фамилия: \t', self.lastname, '\nИмя: \t\t', self.firstname)  # отсутствует отчество
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

    base_humans.pop(0)  # отекаем заголовок
    print('БЕЗ ДУБЛИКАТОВ')
    base_humans2 = merge_duplicate(base_humans)
    for i in base_humans2:
        i.show_base()

    new_contact_list = make_new_contact_list(base_humans2)
    pprint(contacts_list)
    print()
    pprint(new_contact_list)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        f.writelines(new_contact_list)
