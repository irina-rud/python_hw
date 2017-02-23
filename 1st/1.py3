import sys
x = 0
try:
    x = int(input())
except ValueError:
    print('Invalid Number')

result = 1
previous = 0
if( x == 0):
    print(0)
elif( x == 1):
    print(1)
else:
    for i in range(2,x + 1):
        previous, result = result, result + previous
    print(result)