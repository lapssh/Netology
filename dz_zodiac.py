"""Задание №3
Разработать приложение для определения знака зодиака по дате рождения.
Пример:
Введите месяц: март
Введите число: 6
Вывод:
Рыбы
"""
# Запрашиваем у пользователя исходные данные
month = input('Введите месяц: ')
number = int(input('Введите число: '))

# Вычисляем знак зодиака
if number >= 21 and month == 'март':
    zodiac = 'Овен'
elif number <= 20 and month == 'апрель':
    zodiac = 'Овен'
elif number >= 21 and month == 'апрель':
    zodiac = 'Телец'
elif number <= 20 and month == 'май':
    zodiac = 'Телец'
elif number >= 21 and month == 'май':
    zodiac = 'Близнецы'
elif number <= 20 and month == 'июнь':
    zodiac = 'Близнецы'
elif number >= 21 and month == 'июнь':
    zodiac = 'Рак'
elif number <= 22 and month == 'июль':
    zodiac = 'Рак'
elif number >= 23 and month == 'июль':
    zodiac = 'Лев'
elif number <= 22 and month == 'август':
    zodiac = 'Лев'
elif number >= 23 and month == 'август':
    zodiac = 'Дева'
elif number <= 23 and month == 'сентябрь':
    zodiac = 'Дева'
elif number >= 24 and month == 'сентябрь':
    zodiac = 'Весы'
elif number <= 23 and month == 'октябрь':
    zodiac = 'Весы'
elif number >= 24 and month == 'октябрь':
    zodiac = 'Скорпион'
elif number <= 21 and month == 'ноябрь':
    zodiac = 'Скорпион'
elif number >= 22 and month == 'ноябрь':
    zodiac = 'Стрелец'
elif number <= 21 and month == 'декабрь':
    zodiac = 'Стрелец'
elif number >= 22 and month == 'декабрь':
    zodiac = 'Козерог'
elif number <= 19 and month == 'январь':
    zodiac = 'Козерог'
elif number >= 22 and month == 'январь':
    zodiac = 'Водолей'
elif number <= 18 and month == 'февраль':
    zodiac = 'Водолей'
elif number >= 19 and month == 'февраль':
    zodiac = 'Рыбы'
elif number <= 20 and month == 'март':
    zodiac = 'рыбы'
else:
    zodiac = 'Вы ввели какую-то шляпу'

print(zodiac)
