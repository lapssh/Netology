import csv
import re
import datetime
from pymongo import MongoClient




def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    collection = db['artists-collection']
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        event = list()
        for row in reader:
            tmp_date = row['Дата'].split('.')
            row['Дата'] = datetime.datetime(year=2020, month=int(tmp_date[1]), day=int(tmp_date[0]))
            row['Цена'] = int(row['Цена'])
            event.append(row)
    collection.insert_many(event)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    result = db['artists-collection'].find().sort('Цена', 1)
    for row in result:
        print(row)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    pattern = '\\w*\\s' + name + '\\w*'
    regex = re.compile(pattern)
    result = db['artists-collection'].find({'Исполнитель': regex}).sort('Цена', 1)
    for row in result:
        print(row)


def event_in_period(db, start_date, end_date):
    print('Мероприятия по нужному интервалу:', start_date, ' - ', end_date)
    event = db['artists-collection'].find({'$and': [
        {'Дата': {'$gte': datetime.datetime(year=2020, month=int(start_date[3:]), day=int(start_date[:2]))}},
        {'Дата': {'$lte': datetime.datetime(year=2020, month=int(end_date[3:]), day=int(end_date[:2]))}}
    ]})
    for row in event:
        print(row)


if __name__ == '__main__':
    file_name = 'artists.csv'
    client = MongoClient()
    db = client['artists_database']
    #read_data(file_name, db)
    print('Результат сортировки по цене:')
    find_cheapest(db)
    rock_star_name = 'Шуф'
    # rock_star_name = input('Введите имя исполнителя: ')
    print('Поиск по имени Шуф:')
    find_by_name(rock_star_name, db)
    event_in_period(db, '01.07', '30.07')
