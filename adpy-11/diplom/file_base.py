def add_user(id, kpi, data):
    data += '\n'
    with open('fdatabase.txt', 'a', encoding='utf-8') as f:
        f.write(data)
