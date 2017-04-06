import os
import sys


def main():
    if len(sys.argv) <= 1:
        print "Usage:", sys.argv[0], "<dir path>"
        return

    dir = sys.argv[1]
    filedata = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if not os.path.isfile(path):
            continue
        st = os.stat(path)
        filedata.append([name, st.st_size])

    filedata.sort(key=lambda x: (-x[1], x[0]))
    for name, size in filedata:
        print name + '\t' + str(size)

main()
