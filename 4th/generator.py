import sys
from functools import wraps


class GeneratorWrapper(object):
    def __init__(self, generator, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.generator = generator(*args, **kwargs)
        self.generator_begin = generator

    def __next__(self):
        try:
            return next(self.generator)
        except StopIteration:
            self.generator = self.generator_begin(*self.args, **self.kwargs)
            raise StopIteration

    def __iter__(self):
        return self

    def __call__(self):
        return self


def inexhaustible(gen):
    @wraps(gen)
    def inner(*args, **kwargs):
        return GeneratorWrapper(gen, *args, **kwargs)
    return inner


exec(sys.stdin.read())
