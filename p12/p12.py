def nth_triangle(n): return n*(n+1)/2

def triangle_gen(n):
    current = nth_triangle(n)
    while 1:
        yield current
        n += 1
        current += n

def find_n(x):
    import math
    x *= 2
    n = 0.5 * (-1 + math.sqrt(1 + 4*x))
    return n

def is_triangle(x):
    n = find_n(x)
    return n == int(n)

import factors
def count_factors(x):
    return len(factors.factors(x))
