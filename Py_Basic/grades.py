class8 = [3,4,5,4,3,3,2,1]
class9 = [5,2,5,2,3,1,2,1]
class10 = [3,4,5,4,4,5,5,5]

school = [class8,class9,class9]
max_grade = 0
for index, i  in enumerate(school):
    avg = sum(i) / len(i)
    if avg > max_grade:
        max_grade = avg

print(f'Лучшая средняя оценка')

