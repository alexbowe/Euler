from rabin_miller import is_prime_rm
is_prime = is_prime_rm

def num_digits(n):
    import math
    return int(math.ceil(math.log(n+1, 10)))

def cycle(n,places=None):
    places = places or num_digits(n)
    t = n%10
    n /= 10
    return n + t*10**(places-1)

def cycles(n):
    for i in xrange(num_digits(n)):
        yield n
        n = cycle(n)

def circular_prime(n,k=100):
    if n <= 1: return False
    for c in cycles(n):
        if not is_prime(c,k):
            return False
    return True

if __name__ == '__main__':
    count = 1
    for n in xrange(3, 1000000, 2):
        if circular_prime(n, 5):
            count += 1

    print count
