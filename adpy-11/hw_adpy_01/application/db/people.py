from application.db.data_employees import employees
def get_employees():
    print('\nСработал вызов функции get_empployees() из модуля people.py')
    print('\nВ нашей компании всё еще работают эти сотрудники:')
    for person in employees.values():
        print(person)
