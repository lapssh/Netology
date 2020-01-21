# Задача №1
# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту
# и познакомим людей с одинаковыми индексами после сортировки! "Познакомить" пары нам поможет функция zip,
# а в цикле распакуем zip-объект и выведем информацию в виде:
#
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить не будет и выведем
# пользователю предупреждение, что кто-то может остаться без пары!
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# пресет для теста, когда парней больше
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Maksim', 'Garry', 'Willie']
boys.sort()
# print(boys)
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Sirena']# пресет для теста когда парней больше
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Sirena', 'Anna', 'Elsa', 'Penelopa']
girls.sort()

if len(boys) > len(girls):
    num = len(boys) - len(girls)
    num_for_pair = len(boys) - num
    loosers = boys[num_for_pair:]
    print('Эти неудачники останутся без девченок: ', loosers)
    print('Зато у нас есть........')

if len(girls) > len(boys):
    num = len(girls) - len(boys)
    num_for_pair = len(girls) - num
    loosers = girls[num_for_pair:]
    print('Самые страшные, кто останутся одинокими: ', loosers)
    print('Зато у нас есть........')

arch = zip(boys, girls)
print('Идеальные пары:')
for pair in list(arch):
    print(f'{pair[0]} и {pair[1]}')
