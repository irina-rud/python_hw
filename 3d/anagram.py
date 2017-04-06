#!/usr/bin/env python3


def main():
    n = int(input())
    dictionary = dict()
    for i in range(n):
        line = input().strip().lower()
        key_line = str(sorted(line))
        if key_line not in dictionary.keys():
            dictionary[key_line] = set()
        dictionary[key_line].add(line)
    output = []
    for key in dictionary.keys():
        if len(dictionary[key]) > 1:
            new_line = ' '.join(sorted(dictionary[key]))
            output.append(new_line)
    output = sorted(output)
    for line in output:
        print(line)


if __name__ == '__main__':
    main()
