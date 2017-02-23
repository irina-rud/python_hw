import sys

N = 0
try:
    N = int(input())
except ValueError:
    print('Invalid Number')
    
for i in range(N):
    s = input()
    result = ""
    for a in range(1,len(s) + 1):
        for b in range(0,len(s) - a + 1):
            result += s[b:b+a] + " "
    print(result[:-1])