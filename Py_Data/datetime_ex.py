from datetime import datetime
def check_date(stream):
    try:
        for i in stream:
            print(i)
            d = datetime.strptime(i, '%Y-%m-%d')
            print(d, '- True')
    except ValueError:
        print(i, '- False')

stream = ['2018-04-02', '2018-02-29', '2018-19-02']
check_date(stream)