import itertools

def coprime_by(x, factors):
    for factor in factors:
        if x % factor is 0:
            return False
    return True

def sieve_stackless():
    factors = [2]
    x = 3
    yield 2
    while True:
        if coprime_by(x, factors):
            factors.append(x)
            yield x
        x += 2

def prime_factors(v):
    if v == 1: return
    for p in sieve_stackless():
        if v < p: break
        if v % p is 0:
            yield p
            v /= p

n = 600851475143
print list(prime_factors(n))[-1]
