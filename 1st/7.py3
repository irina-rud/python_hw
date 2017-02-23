import sys

# f = open('text.txt')
# line = f.readline()
# limit = int(line)
# line = f.readline()
# while(line):
limit = int(input())

for line in sys.stdin:
    words = line.split()
    to_print = []
    for word in words:
        if len(word) >= limit:
            to_print.append(word)
        elif len(to_print) == 0:
            to_print.append(word)
        else:
            if len(word) + len(to_print[-1])  + 1 <= limit:
                to_print[-1] += " " + word
            else:
                to_print.append(word)

    for i in range(len(to_print)):
        print(to_print[i])
    if (len(to_print) == 0):
        print()
