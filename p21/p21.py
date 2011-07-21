from factors import factors

def d(n):
    return sum(factors(n)[:-1])

nums = range(0, 10000)
sums = map(d, nums)
lookup = dict()
for (a, s) in enumerate(sums):
    if s in lookup:
        lookup[s].add(a)
    else:
        lookup[s] = set()
        lookup[s].add(a)

amics = set()
for (a, b) in enumerate(sums):
    if a < 2 or a == b: continue
    if a in lookup and b in lookup[a]:
        amics.add(a)
        amics.add(b)

print sum(amics)
