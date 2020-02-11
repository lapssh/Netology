import datetime


class Mylog:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'at')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

def factorial_n(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


with Mylog ('myfile.txt') as file:

    start_time = datetime.datetime.now()
    print('Программа начала своё выполнение в ', start_time)
    file.write(str(start_time)+ '\n')
    result = factorial_n(99999)
    finish_time = datetime.datetime.now()
    time_to_calculate = finish_time-start_time

    print(f'Факториал числа 99999 данная программа вычисляет за {time_to_calculate} секунды')
    print(f'Программа завершила свою работу ровно в : {finish_time}')
    file.write(str(start_time.minute) + '  ' + str(start_time.second) + '123\n')

