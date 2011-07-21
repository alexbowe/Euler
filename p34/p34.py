import math
digits = range(10)
facts  = map(math.factorial, digits)

def digs(x):
    while x > 0:
        yield x%10
        x/=10

def test(x):
    return x == sum([facts[n] for n in digs(x)])

ns = [n for n in range(3,100000) if test(n)]
print sum(ns)
