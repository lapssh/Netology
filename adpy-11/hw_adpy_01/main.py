import datetime as dt
from dirty_main import *
from application.salary import calculate_salary
from application.db.people import get_employees
if __name__ == '__main__':
    print('Вас приветствует main.py! Вы должны прочитать это первым, или программист налажал.')
    my_date = dt.datetime.today()
    print(f'Сегодня у нас {my_date.strftime("%d.%m.%Y")} ')
    calculate_salary()
    get_employees()