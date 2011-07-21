class FMaker:
    def __init__(self, d):
        self.d = d

    def __call__(self, x):
        return (10**x)/self.d%10

def brent(f, x0):
    # main phase: search successive powers of two
    power = lam = 1
    t_x = x0
    h_x = x0+1 # f(x0) is the element/node next to x0.
    while f(t_x) != f(h_x):
        if power == lam:   # time to start a new power of two?
            t_x = h_x
            power *= 2
            lam = 0
        h_x += 1
        lam += 1
 
    # Find the position of the first repetition of length lambda
    mu = 0
    t_x = h_x = x0
    for i in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
        h_x += 1
    while f(t_x) != f(h_x):
        t_x += 1
        h_x += 1
        mu += 1
 
    return lam, mu


def floyd(f, x0):
    # The main phase of the algorithm, finding a repetition x_mu = x_2mu
    # The hare moves twice as quickly as the tortoise
    t_x, h_x = x0 + 1, x0 + 2
    while f(t_x) != f(h_x):
        t_x += 1
        h_x += 2

    # at this point the start of the loop is equi-distant from current tortoise
    # position and x0, so hare moving in circle and tortoise (set to x0 )
    # moving towards circle, will intersect at the beginning of the circle.
 
    # Find the position of the first repetition of length mu
    # The hare and tortoise move at the same speeds
    mu = 0
    t_x = x0
    while f(t_x) != f(h_x):
        t_x += 1
        h_x += 1
        mu += 1
 
    # Find the length of the shortest cycle starting from x_mu
    # The hare moves while the tortoise stays still
    lam = 1
    h_x = t_x + 1
    while f(t_x)!= f(h_x):
        h_x = h_x + 1
        lam += 1
 
    return lam, mu

def brute_force():
    m = 0
    d = 0
    for i in xrange(2, 100):
        f = FMaker(i)
        (l, _) = floyd(f, 1)
        if l > m:
            m = l
            d = i
    print d, m

if __name__ == '__main__':
    from rabin_miller import is_prime
    p = 7
    for i in xrange(999, 7, -2):
        if is_prime(i, 3):
            p = i
            break
    (l, _) = floyd(FMaker(p), 1)
    print p, l
