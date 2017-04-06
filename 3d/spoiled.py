import re

rus = 'йцукенгшщзхъёэждлорпавыфячсмитьбю'
russ_let = ','.join(rus)

pattern = re.compile(
                        '\s*([0-9]{4}(\.[0-9]{2}\.' +
                        '|-[0-9]{2}-' +
                        '|/[0-9]{2}/)[0-9]{2}' +
                        '|[0-9]{2}(\.[0-9]{2}\.' +
                        '|-[0-9]{2}-' +
                        '|/[0-9]{2}/)[0-9]{4}' +
                        '|[0-9]{1,2}\s*[' + rus + ']+\s*[0-9]{4}' +
                        ')\s*')

while True:
    try:
        s = input()
        if s == '':
            break
    except:
        break
    match = pattern.match(s)
    try:
        if match.start() == 0 and match.end() == len(s):
            print('YES')
        else:
            print('NO')
    except:
        print('NO')

'''
2006.05.04 V
2006-05-04 V
2006/05/04 V
04.05.2006 V
04-05-2006 V
04/05/2006 V
4 мая 2006 V
4мая2006 V
adcd
12.34.56
5 мая июня
1000 июня 03
'''