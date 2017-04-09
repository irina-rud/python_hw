import re

pattern = re.compile(
    '((;|\n)\t* *import( +[^ ,,\t,\n,;]+\,)*' +
    '( +[^ ,\t,\n,;]+) *|(\;|\n)\t* *from +[^ ,\n,\t,;]+ +)')


def search_results(pattern, text):
    return pattern.finditer(text)


ans = set()

h = '\n'
while True:
    try:
        s = input()
        # print(s)
        h += (s + '\n')
    except:
        break

res = search_results(pattern, h)
for m in res:
    for y in m.group().split()[1:]:
        if y == 'import':
            continue
        if y[-1] == ',' or y[-1] == ';':
            y = y[:-1]
        ans.add(y)
print(', '.join(sorted(ans)))