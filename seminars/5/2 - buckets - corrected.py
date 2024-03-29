import sys
from copy import copy


class Buckets(object):
    def __init__(self, length, default):
        self.default = copy(default)
        self.buckets = [copy(self.default) for i in range(length)]

    def add(self, index, element):
        self.buckets[index].append(element)

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = copy(self.default)


if __name__ == '__main__':
    exec(sys.stdin.read())
