lim = 10**9

def s(a, b, c):
    a %= lim
    b %= lim
    c %= lim

    lookup = [None] * lim

    def f(n):
        n %= lim
        if lookup[n]: return lookup[n]
        if n>b: return (n - c) %lim
        return f(a + f(a + f(a + f(a + n)))) % lim

    ans = 0
    for x in xrange(b+1):
        x = f(x)
        x %= lim
        ans += x
        ans %= lim

    return ans


a,b,c = 21**7, 7**21, 12**7
#a,b,c = 50,2000,40
a,b,c = 10,20,30
print s(a, b, c)
