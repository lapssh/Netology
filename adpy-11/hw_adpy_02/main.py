import requests, json

WIKI_LINK = 'https://en.wikipedia.org/wiki/'


class TrueIterator:
    def __init__(self, data):
        self.end = len(data)
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.end:
            raise StopIteration
        return self.data[self.index]


if __name__ == '__main__':
    with open('countries.json') as f:
        data = json.load(f)
        for country in TrueIterator(data):
            print(country['name']['official'])
            country_link = WIKI_LINK + country['name']['official']
            response = requests.get(country_link)
            if response.status_code != 200:
                with open('country-wiki.txt', 'at', encoding='utf-8') as f2:
                    f2.write(country['name']['official'] + '\t-\t На википедии такой страны не найдено\n')
            else:
                with open('country-wiki.txt', 'at', encoding='utf-8') as f2:
                    f2.write(country['name']['official'] + '\t-\t' + country_link + '\n')
            print(response)
