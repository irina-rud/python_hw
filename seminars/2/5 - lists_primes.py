def primes(n):
    return [i for i in range(2, n) if i not in
            [p * c for p in range(2, n) for c in range(2, n)]]


def primes_another(n):
    return [i for i in range(2, n) if
            len([d for d in range(2, i) if i % d == 0]) == 0]


print primes(50)
print primes_another(50)
