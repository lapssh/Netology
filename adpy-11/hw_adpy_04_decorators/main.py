from datetime import datetime


def decorator(log_path):
    def wrapper(func):
        def logger(*args, **kwargs):
            with open(log_path, 'a', encoding='utf-8') as log_file:
                log_file.write('-' * 60 + '\n')
                log_file.write('Зафиксирован вызов функции ' + str(func.__name__) + '\n')
                log_file.write(datetime.now().strftime('%d.%m.%Y %H:%M') + '\n')
                log_file.write('Список переданных агрументов:' + str(args) + '\n')
                start = datetime.now()
                result = func(*args, **kwargs)
                end = datetime.now()
                working_time = end - start
                log_file.write('Время выполнения функции:' + str(working_time) + '\n')
                log_file.write('-' * 60 + '\n\n')
                return result

        return logger

    return wrapper


@decorator('first.txt')
def bigdata(*args):
    l = [x for x in range(10 ** 7) if x % 2 == 0]
    return l


@decorator('second.txt')
def bigdata2(*args):
    l = [x for x in range(10 ** 7) if x % 2 != 0]
    return l


if __name__ == '__main__':
    l1 = bigdata(1, 2, 3, 4, 5, '99')
    l2 = bigdata2(3, 'hello_python!', 45, .5)
