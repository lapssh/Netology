import random
class Animal:
    def __init__(self, name):
        self.name = name
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


goose_white = Goose('Белый')
goose_grey = Goose('Серый')
print(goose_white.name)
print('Сегодня Серый снес яйца в колличестве: ', goose_grey.get_eggs())