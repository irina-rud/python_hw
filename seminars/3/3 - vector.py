class Vector(object):
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        new_values = [a + b for a, b in zip(self.values, other.values)]
        return Vector(new_values)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([a * b for a, b in zip(self.values, other.values)])
        else:
            new_values = [value * other for value in self.values]
        return Vector(new_values)
        
    __rmul__ = __mul__

    def __repr__(self):
        return ('Vector([' +
                ', '.join([str(val) for val in self.values]) +
                '])')

    def __eq__(self, other):
        return isinstance(other, Vector) and self.values == other.values

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value


def main():
    v1 = Vector([1, 2, 3])
    v2 = Vector([-1, 2, -1])

    print v1 + v2
    print v1 * v2
    print v1 * 0.5
    print 0.5 * v1


main()
