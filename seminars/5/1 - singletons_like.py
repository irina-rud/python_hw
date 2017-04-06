def is_singleton(obj):
    first = eval(repr(obj))
    second = eval(repr(obj))
    return first is second


def main():
    singletons_candidates = (
        [(), [], ''] +
        [chr(i) for i in range(33, 127)] +
        range(-1000, 1000) +
        [0.0, 0 + 0j, 1j]
    )

    singletons = []
    for obj in singletons_candidates:
        if is_singleton(obj):
            singletons.append(obj)

    print singletons

if __name__ == '__main__':
    main()
