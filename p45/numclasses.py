from math import sqrt

def is_triangle(x):
    # x = 0.5 n (n + 1)
    n = 0.5 * (-1 + sqrt(1 + 8*x))
    return n == int(n)

def is_pentagonal(x):
    # x = n(3n-1)/2
    n = (1 + sqrt(1 + 24*x))/6
    return n == int(n)

def is_hexagonal(x):
    # x = n(2n-1)
    n = (1 + sqrt(1 + 8*x))/4
    return n == int(n)
