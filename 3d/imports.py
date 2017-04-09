#!/usr/bin/env python3
from sys import stdin
import re

regexp_1 = r'([\t\s]*import\s+[^)]*)'

regexp_2 = '([\s\t]*from\s+(?P<from>\w+)\s+import\s+[a-zA-Z])'


def main():
    result = set()
    for str in stdin:
        for line in str.split(';'):
            line = line.strip()
            if line != '':
                if line.find('from ') == -1:
                    match1 = re.search(re.compile(regexp_1), line)
                    if match1 is not None:
                        for import_world in re.findall(re.compile(r'[, ]+([^, ]+)'), line):
                            if import_world[-1] == '\n':
                                result.add(import_world[:-1])
                            else:
                                result.add(import_world)
                else:
                    match2 = re.match(regexp_2, line)
                    if match2 is not None:
                        if match2.group('from') is not None:
                            result.add(match2.group('from'))
    print(', '.join(sorted(result)))

if __name__ == '__main__':
    main()
