def fib_gen(limit):
    fibn1, fibn2 = 1, 1
    while fibn2 <= limit:
        yield fibn2
        fibn1, fibn2 = fibn2, fibn1 + fibn2

#ans = sum(x for x in fib_gen(4e6) if x%2 is 0)

def even_fibs(limit):
    import math
    r = math.sqrt(5)
    phi, phi_dash = (1 + r)/2, (1 - r)/2
    b, b_dash = phi**3, phi_dash**3

    k = 1
    while 1:
        fib = int((b**k - b_dash**k)/r)
        if fib > limit: break
        yield fib
        k += 1

ans = sum(x for x in even_fibs(4e6))
print ans
