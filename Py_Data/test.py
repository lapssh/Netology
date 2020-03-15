import re
pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+.[a-zA-Z.]{2,64}$'
test_mails = ['admin@gmail.com', 'support12@yandex.ru', 'MaMa@@family.io.oi', '12admin@12mail.ru']
for i in test_mails:
    if re.match(pattern, i):
        print(i, '- соответствует')
    else:
        print(i, '- не соответствует')