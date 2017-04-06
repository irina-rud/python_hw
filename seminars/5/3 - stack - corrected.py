import sys


class Stack(object):
    def __init__(self, elements=()):
        self.elements = list(elements)

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def __len__(self):
        return len(self.elements)


if __name__ == '__main__':
    exec(sys.stdin.read())
