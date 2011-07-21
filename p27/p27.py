from rabin_miller import is_prime

def count_primes(f, k):
    count = 0
    n = 0
    while 1:
        if is_prime(f(n), k):
            count += 1
        else: return count
        n += 1

if __name__ == '__main__':
    m = 0
    (x, y) = (None, None)
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            f = lambda n: n**2 + a*n + b
            count = count_primes(f, 10)
            if count > m:
                m = count
                (x, y) = (a, b)
    print 'n^2 + %sn + %s -> %s primes' % (x, y, m)
    print x*y
