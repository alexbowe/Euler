import math
r = math.sqrt(5)
phi, phi_dash = (1 + r)/2, (1 - r)/2

def fib(n):
    (1+r)/2
    return int((phi**n - phi_dash**n)/r)

digit_mask = 10**999
def dig_1k(n):
    return n >= digit_mask

def guess(low, high):
    while 1:
        if high <= low:
            return low
        mid = (low + high)/2
        # is the mid > 1k digs?
        if dig_1k(fib(mid)):
            high = mid
        # if not, and high is:
        elif dig_1k(fib(high)):
            low = mid
        # if high isn't, then we should change the range
        else:
            low = high + 1
            high *= 2

#answer = 4782 - used mathematica
