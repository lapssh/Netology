import json
purchases = {}
with open('purchase_log.txt', 'rt', encoding = 'utf-8') as f:
    i = 0
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        if dict_['user_id'] != 'user_id':
            purchases[dict_['user_id']] =  dict_['category']
with open('visit_log.csv', 'a+', encoding='utf-8') as f:
    f.seek(0,0)
    for line in f:
        tmp_line = line.strip()
        id = tmp_line.split(',')[0]
        print(id)
        if id in purchases.keys():
            print('1')
            f.write(','+str(purchases[id]+'\n'))
print('done')