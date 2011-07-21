def prime_factors(value):
    """trial divisions are all primes because of previous reductions of value 
    print list(factors(1234567890987654321))"""
    import itertools
    if value > 3:
        for this in itertools.chain(iter([2]), xrange(3,int(value ** 0.5)+1, 2)):
            if this*this > value:  break
            while not (value % this):
                if value == this: break
                value /=  this
                yield this
    yield value


def prime_factors_mult(n):
    """return list [ [p_0,k_0], [p_1,k_1], ... ], where there are 'k_i'
    occurrences of 'p_i' in the prime factorization of n.

    >>> prime_factors_mult(315)
    [[3, 2], [5, 1], [7, 1]]
    """
    res = list(prime_factors(n))
    return sorted([fact, res.count(fact)] for fact in set(res))

def factors(n):
    all = [1]
    for p, e in prime_factors_mult(n):
        prev = all[:]
        pn = 1
        for i in range(e):
            pn *= p
            all.extend([a*pn for a in prev])        
    all.sort()
    return all
