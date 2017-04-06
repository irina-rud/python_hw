#!/usr/bin/env python3
from sys import stdin
import re

regular_expression = '((\d{4}[-]\d{2}[-]\d{2})'
regular_expression += '|(\d{4}[/]\d{2}[/]\d{2})'
regular_expression += '|(\d{4}[.]\d{2}[.]\d{2})'

regular_expression += '|(\d{2}[-]\d{2}[-]\d{4})'
regular_expression += '|(\d{2}[/]\d{2}[/]\d{4})'
regular_expression += '|(\d{2}[.]\d{2}[.]\d{4})'

regular_expression += '|(\d{1,2}\s*['
regular_expression += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
regular_expression += ']+\s*\d{4}))$'


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
