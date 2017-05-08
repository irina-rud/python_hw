#!/usr/bin/env python3
import sys


def unique(arr):
    previous = None
    for element in arr:
        if element != previous:
            yield element
        previous = element

exec(sys.stdin.read())
