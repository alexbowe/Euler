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

def get_nth_prime(n):
    primes = sieve_stackless()
    prime = 0
    for i in xrange(n):
        prime = primes.next()
    return prime

print get_nth_prime(10001)
