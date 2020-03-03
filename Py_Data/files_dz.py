import json
import os
purchases = {}
with open('purchase_log.txt', 'r+', encoding = 'utf-8') as f:
    i = 0
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        if dict_['user_id'] != 'user_id':
            purchases[dict_['user_id']] =  dict_['category']
os.remove('test_date.txt')
with open('visit_log.csv', 'r+', encoding='utf-8') as f:
    for line in f:
        tmp_line = line.strip()
        id = tmp_line.split(',')[0]
        with open('test_date.txt', 'at', encoding='utf-8') as f2:
            if id in purchases.keys():
                f2.write(tmp_line+','+str(purchases[id]+'\n'))
            else:
                f2.write(tmp_line+'\n')
print('done')