# what is the smallest pos num that is evenly divisible by all of the numbers from
# 1 to 20?

def gcd(a,b):
    while b: 
        a, b = b, a % b 
    return a

def lcm(a, b):
    return int(float(a)/gcd(a, b) * b)

def lcm_list(factors):
    l = factors[1]
    for x in factors[1:]:
        l = lcm(l, x)
    return l

f = range(2,21)
print lcm_list(f)

