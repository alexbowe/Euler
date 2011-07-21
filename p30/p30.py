digits = range(10)
powers = [x**5 for x in digits]
print powers

# taken from http://oeis.org/A023052/list
ns = [153,370,371,407,1634,4150,
 4151,8208,9474,54748,92727,93084,194979,548834,
 1741725,4210818,9800817,9926315,14459929,24678050,
 24678051,88593477,146511208,472335975,534494836,
 912985153]

def dig(n):
    while n > 0:
        yield n%10
        n/=10

def test(n):
    return n == sum([powers[x] for x in dig(n)])

result = filter(test, ns)
#result = filter(test, range(4150, 999999))
print sum(result)

# x0^5 + x1^5 + ... + x(n-2)^5 + x(n-1)^5 = x0 * 10^(n-1) + x1 * 10^(n-2) + ... + xn * 0

# x0^4 + x1^4 + x2^4 + x3^4 == x0 * 10^0 + x1 * 10^1 + x2 * 10^2 + x3 * 10^3

# n%10 + (n/10)%10 + (n%10 + ... n%10^n = 
# n + n/10 + n/100 + ... + n * 10^-(n-1)

# 3 digits:
# a b c
# a^p + b^p + c^p == a * 100 + b * 10 + c
# 100a + a^p + 10b + b^p + c + c^p = 0
# a(100 + a^(p-1)) + b(10 + b^(p-1)) + c(1 + c^(p-1)) = 0
# 1000...
# keep adding them to find out what the next one should be?

# (10^i)a + a^p = 

# n * 10 + a == a^5


