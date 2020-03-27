import hashlib


def calculator_md5(file):
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            yield hashlib.md5(line.encode()).hexdigest()


for i in calculator_md5('hash_strings.txt'):
    print(i)
