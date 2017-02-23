import sys
import operator

st = ''
for line in sys.stdin:
    st += line 
l = list(st.lower().strip())
l = list(filter(lambda ch:ch.isalpha(),l))

dictionary = dict()
for ch in l:
    if (ch in dictionary.keys()):
        dictionary[ch] -=1
    else:
        dictionary[ch] = -1
sorted_d = sorted(dictionary.items(), key=operator.itemgetter(1, 0))
for pair in sorted_d:
    print("%s: %s" % (pair[0],abs(pair[1])))