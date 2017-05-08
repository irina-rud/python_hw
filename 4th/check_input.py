import sys
from functools import wraps


def takes(*types):
    def check_accepts(f):
        @wraps(f)
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError
            return f(*args, **kwds)
        new_f.func_name = f.func_name
        return new_f
    return check_accepts

exec(sys.stdin.read())
