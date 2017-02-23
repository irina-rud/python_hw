import sys

p = 0
try:
    p = float(input())
except ValueError:
    print('Invalid Number')
result = 0

inp = input()
vect = inp.split()
for line in vect:    
    try:
        n = abs(float(line))
    except ValueError:
        print('Invalid Number')
    result += n ** p
print( '%f' % result**(1/p))
