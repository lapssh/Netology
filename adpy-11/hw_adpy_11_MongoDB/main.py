import csv
import re
import datetime
from pprint import pprint

from pymongo import MongoClient


# def read_data(csv_file, db):
#     """
#     Загрузить данные в бд из CSV-файла
#     """
#     with open(csv_file, encoding='utf8') as csvfile:
#         # прочитать файл с данными и записать в коллекцию
#         reader = csv.DictReader(csvfile)
#     return reader
def read_data(csv_file):
    """
    Загрузить данные в бд из CSV-файла
    """
    client = MongoClient()
    db = client['artists_database']
    collection = db['artists-collection']
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        event = list()
        for row in reader:
            print(row)
            event.append(row)
    first_post = {'Исполнитель': 'Louna', 'Цена': '9999', 'Место': 'На крыше кремля', 'Дата': '29.04'}
    first_post_id = collection.insert_one(first_post).inserted_id
    #db.collection_names(include_system_collections=False)
    result = collection.insert_many(event)
    print(result.inserted_ids)
    #return event

def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """

    regex = re.compile('укажите регулярное выражение для поиска. ' \
                       'Обратите внимание, что в строке могут быть специальные символы, их нужно экранировать')


if __name__ == '__main__':

    # client = MongoClient()
    # db = client['artists_db']
    file_name = 'artists.csv'
    read_data(file_name)
    # client = MongoClient()
    # db = client['test-database']
    # collection = db['test-collection']
    # post = {"author": "Mike",
    #         "text": "My first blog post!",
    #         "tags": ["mongodb", "python", "pymongo"],
    #         "date": datetime.datetime.utcnow()}
    # posts = db.posts
    # post_id = posts.insert_one(post).inserted_id
    #db.collection_names(include_system_collections=False)


