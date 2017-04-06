class ProductSet(object):
    def __init__(self, elements, size):
        self.elements = elements
        self.size = size
        self.current_set_indexes = [0 for _ in xrange(self.size)]

    def current_set(self):
        return [self.elements[index] for index in self.current_set_indexes]

    def next(self):
        index_pos = 0
        self.current_set_indexes[index_pos] += 1
        while self.current_set_indexes[index_pos] >= len(self.elements):
            self.current_set_indexes[index_pos] = 0
            if index_pos < self.size - 1:
                index_pos += 1
                self.current_set_indexes[index_pos] += 1


def main():
    s = ProductSet([1, 'a'], 2)
    for _ in range(7):
        print s.current_set()
        s.next()


main()
