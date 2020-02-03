import random


class Animal: #Родительский класс для всех животинок на ферме
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        """
        Кормим  животинку
        :return:
        """
        fat = round(self.weight * 0.05,1)
        self.weight += fat
        print(f'Животинка {self.name} покушала и сказала {self.golos}')
        print(f'К тому же немного потолстела  на {fat} килогамма')
    golos = '*(&^*&^#@'

class Goose(Animal):
    golos = 'Га-га-га.....'
    def get_eggs(self):
        return print(f'{self.name} снесла',random.randint(0, 5), ' яиц')


class Duck(Goose):
    golos = 'Кря.... Кря.... Кря.... Утиная типизация, все дела.... Кря....'
    def get_eggs(self):
        return print(f'{self.name} снесла  ',random.randint(0, 3), ' яиц')


class Chicken(Goose):
    golos = 'Ко-ко-ко.... '
    def get_eggs(self):
        return print(f'{self.name} снесла  ',random.randint(0, 10), ' яиц')


class Cow(Animal):
    golos = "Му----Мууу-Муууууууууу"
    def get_milk(self):
        return print(f'Подоив {self.name} мы получили',random.randint(30, 90), 'литров молока ')


class Goat(Cow):
    golos = 'Бе-е-е-е-е-е, Бе-е-е-е-е-е-е-е'
    def get_milk(self):
        return print(f'Подоив {self.name} мы получили',random.randint(1, 5), 'литров молока ')


class Sheep(Animal):
    golos = 'Мы бе-е-е-е-е-дны-е-е-е-е-е-е   ове-е-е-е-е-чки'
    def shear_sheep(self):
        return print(f'После стрижки {self.name} у нас получилось',random.randint(1, 4), 'килогамма шерсти')


goose_white = Goose('Белый', 3)
goose_grey = Goose('Серый', 3)
chicken01 = Chicken('Ко-Ко', 1.4)
chicken02 = Chicken('Кукареку', 1.9)
duck01 = Duck('Кряква', 2.4)
cow01 = Cow('Манька', 500)
goat01 = Goat('Рога', 80)
goat02 = Goat('Копыта', 85)
sheep01 = Sheep('Барашек', 110)
sheep02 = Sheep('Кудрявый', 123)

# Гуси
print('Добро пожаловать на ферму Дядюшки Джо!')
print('Здесь у нас Гуси - пора их покормить..')
goose_white.feed()
goose_grey.feed()
print('А пока они кушают, мы соберем яйца (и да, я знаю, что гуси не несут яйца....)')
goose_grey.get_eggs()
goose_white.get_eggs()
print('-----------------------------------------------------------------------------------')
# Коровка
print('А сколько корова дает молока?')
cow01.get_milk()
print('Покормим нашу буренку.')
cow01.feed()
print('-----------------------------------------------------------------------------------')
# Утка
print('А тут у нас уточка, накомим же её')
duck01.feed()
duck01.get_eggs()
print('-----------------------------------------------------------------------------------')
# Куры
print('Здесь у нас курочка и петушок')
chicken01.feed()
chicken02.feed()
chicken02.get_eggs()
chicken01.get_eggs()
print('-----------------------------------------------------------------------------------')
# Козы
print('Здесь у нас козы')
goat01.feed()
goat02.feed()
goat01.get_milk()
goat02.get_milk()
print('-----------------------------------------------------------------------------------')
# Овцы
print('Нам осталось только покормить и подстричь овец')
sheep01.feed()
sheep02.feed()
sheep01.shear_sheep()
sheep02.shear_sheep()

# Считаем общий вес животных на ферме
all_weight = goose_grey.weight + goose_white.weight + chicken01.weight + chicken02.weight + (
        duck01.weight + cow01.weight + goat01.weight + goat02.weight + sheep01.weight + sheep02.weight
)
all_weight = round(all_weight, 1)
print('-----------------------------------------------------------------------------------')
print(f'Вес всех животинок на ферме уже перевалил за {all_weight} килограмм.')
