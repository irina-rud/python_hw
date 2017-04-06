#!/usr/bin/env python3
from sys import stdin
import string
import re


def is_palindrome(line):
    line = line.lower()
    line = ''.join(list(map(lambda c: c if c.isalpha() else '', line)))
    line = line.replace('ё', 'е')

    if (line.strip() == line.strip()[::-1]) and line.strip().isalpha():
        print('yes')
    else:
        print('no')


def main():
    n = int(stdin.readline())
    for i in range(n):
        line = stdin.readline()
        is_palindrome(line)


if __name__ == '__main__':
    main()
