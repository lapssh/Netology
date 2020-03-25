from application.db.data_employees import salary, employees
def calculate_salary():
    print('Была вызвана функция calculate_salary из модуля salary.py')
    print('\nЗаработная плата сотрудников:')
    for keys,values in salary.items():
        print(employees[keys], values)