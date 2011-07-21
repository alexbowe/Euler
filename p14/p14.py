lookup = {}
def collatz(n):
    n_original = n
    if n in lookup: return lookup[n]
    terms = 1
    while n > 1:
        if n in lookup:
            ans = lookup[n_original] = terms + lookup[n]
            return ans
        if n%2 == 0: n = n/2
        else: n = 3*n + 1
        terms += 1
    lookup[n_original] = terms
    return terms

m = 0
n = 0
for x in range(1, int(1e6)):
    terms = collatz(x)
    if terms >= m:
        m = terms
        n = x

print n, m
print len(lookup)
