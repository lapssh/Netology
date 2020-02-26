import os
files_count = 0
count_strings = 0
for root, dirs, files in os.walk("M://Garbage/ais"):
    for filename in files:
        if filename[-3:] == '.cs':
            files_count += 1
            # print(filename)
            qqq = os.path.join(root, filename)
            my_file_name = qqq.replace('\\', '/')
            with open(my_file_name,'rt', encoding='utf-8') as f:
                temp = len(f.readlines())
                count_strings += temp


print('Всего в проекте ', files_count, 'файлов с кодом')
print('А написано', count_strings, 'строк кода')



