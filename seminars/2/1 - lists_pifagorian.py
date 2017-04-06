def pifagorian_triplets(upper_bound):
    return [[a, b, c] for a in range(1, upper_bound)
            for b in range(1, upper_bound)
            for c in range(upper_bound)
            if a ** 2 + b ** 2 == c ** 2]


print pifagorian_triplets(20)
