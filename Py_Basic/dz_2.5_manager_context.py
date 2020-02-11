import datetime, random


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

def mega_random(n):
    count_n = 0
    secret_number = random.randint(1, n)
    while True:
        number = random.randint(1, n)
        count_n += 1
        if number == secret_number:
            print("Число неудачных попыток: ", count_n)
            return secret_number, count_n

def mat_generate():
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщьъэюя')
    print(len(alphabet))
    print(alphabet)
    mat = 'лажа'
    count = 0
    while True:
        for i in range(0,3):
            slovo = (alphabet[random.randint(0,31)] + alphabet[random.randint(0,31)]+ alphabet[random.randint(0,31)]
                + alphabet[random.randint(0,31)])
            count += 1
        if mat == slovo:
            print('Попыток было ', count)
            return slovo




with Mylog ('myfile.txt') as file:

    start_time = datetime.datetime.now()
    print(mat_generate())
    finish_time = datetime.datetime.now()
    time_to_calculate = finish_time-start_time
    print(f'Изобретение этого слова потребовало {time_to_calculate}')
    start_time = datetime.datetime.now()
    print('Программа начала своё выполнение в ', start_time)
    file.write(str(start_time)+ '\n')
    result = factorial_n(99999)
    finish_time = datetime.datetime.now()
    time_to_calculate = finish_time-start_time

    print(f'Факториал числа 99999 данная программа вычисляет за {time_to_calculate} секунды')
    print(f'Программа завершила свою работу ровно в : {finish_time}')
    file.write(str(start_time.minute) + '  ' + str(start_time.second) + '123\n')

    n = 1000000
    print('А теперь пуская железяка попробует отгадать случайно число от 0 до ', n)
    start_time = datetime.datetime.now()
    secret, score  = mega_random(n)
    finish_time = datetime.datetime.now()
    time_to_calculate = finish_time-start_time
    print(f'Программа сама себе загадала число {secret} и отгадала его за {time_to_calculate} секунды c {score}')
    print(f'Программа завершила свою работу ровно в : {finish_time}')




