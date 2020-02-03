import random
class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def feed(self):
        """
        Кормим  животинку
        :return:
        """
        print('Животинка радуется...')

class Goose(Animal):
    def get_eggs(self):
        return random.randint(0,5)

class Duck(Goose):
    pass

class Chicken(Goose):
    def get_eggs(self):
        return random.randint(0,10)

class Cow(Animal):
    yield_of_milk = 90
    def get_milk(self):
        return random.randint(yield_of_milk/3, yield_of_milk)


goose_white = Goose('Белый', 3)
goose_grey = Goose('Серый', 3)
chicken01 = Chicken('Ко-Ко', 1.4)
chicken02 = Chicken('Кукареку', 1.9)
cow01 = Cow('Манька', 500)

print(goose_white.name)
print('Сегодня Серый снес яйца в колличестве: ', goose_grey.get_eggs())

print('А сколько корова дает молока?')
print(cow01.get_milk())