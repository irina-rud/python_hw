#!/usr/bin/env python3
from sys import stdin
import re

regular_expression = '(from\s+[a-zA-Z]\s+import\s+[a-zA-Z])'


def main():
    for line in stdin:
        if line.strip != '':
            match = re.match(regular_expression, line)
            if match is not None:
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()
