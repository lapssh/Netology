class Contact:
    def __init__(self, first_name, last_name, number, favorite_contact=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.favorite_contact = favorite_contact
        self.kwargs = kwargs

    def __str__(self):
        pretty_output = 'Имя: ' + self.first_name + '\nФамилия: ' + self.last_name
        if not self.favorite_contact:
            pretty_output += '\nВ избранных: нет'
        else:
            pretty_output += '\nВ избранных: да'
        pretty_output += '\nДополнительная информация:\n'
        for key, value in self.kwargs.items():
            pretty_output += '\t' + key + ' : ' + value + '\n'
        return pretty_output


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}

    def add_new_contact(self, first_name, last_name, number, favorite_contact=False, **kwargs):
        self.contacts[first_name] = Contact(first_name, last_name, number, favorite_contact, **kwargs)

    def show_contacts(self):
        for user in self.contacts.values():
            print(user)

    def delete_contact(self, number):
        for user in self.contacts.values():
            if user.number == number:
                print('YES - мы нашли', number, ' у пользователя ', user.first_name)
                self.contacts.pop(user.first_name)
                break

    def find_favorite_contacts(self):
        for user in self.contacts.values():
            if user.favorite_contact:
                print('Мы нашли в избранном номер: ', user.number, '. Он принадлежит ', user.first_name)

    def find_by_first_name_and_lapst_name(self, first_name, last_name):
        for user in self.contacts.values():
            if user.first_name == first_name:
                if user.last_name == last_name:
                    print('Контакт с именем: ', first_name, ' ', last_name, ' найден')
                    print('Вывожу всю известную информацию....')
                    print(user)
                    return
        print('В наших записях такой нет данных на: ', first_name, ' ', last_name)


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', favorite_contact=True, telegram='@jhony', email='jhony@smith.com')
    print(jhon)

    my_phone_book = PhoneBook('IronMan')
    my_phone_book.add_new_contact('Sarah', 'Connor', '+792655544466', telegram='@connor', email='sarah@connor.ru')
    my_phone_book.add_new_contact('John', 'Connor', '+79115435555', telegram='@lead_minkind', email='john@connor.ru')
    my_phone_book.add_new_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    my_phone_book.add_new_contact('Terminator', 'T-101', '112', favorite_contact=True, telegram='@terminator',
                                  email='t-101@skynet.com')
    my_phone_book.add_new_contact('Super_Terminator', 'T-1000', '007', favorite_contact=True,
                                  telegram='@super_terminator', email='t-1000@skynet.com')
    my_phone_book.show_contacts()
    my_phone_book.delete_contact('+792655544466')
    print('вывдем контакты после удаления Сары')
    my_phone_book.show_contacts()
    print('а теперь поищем избранные номера')
    my_phone_book.find_favorite_contacts()
    my_phone_book.find_by_first_name_and_lapst_name('John', 'Connor')
    my_phone_book.find_by_first_name_and_lapst_name('Электроник', 'Безымянный')
