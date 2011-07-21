from factors import factors

smallest = 12
limit = 28123

def is_abundant(n):
    f = factors(n)[:-1]
    return sum(f) > n

abundants = set()

for x in xrange(smallest, limit+1):
    if is_abundant(x):
        abundants.add(x)

# would be better if i had an ordered set
def sum_of_two_abs(n):
    for a in abundants:
        if a > n: continue
        if (n - a) in abundants:
            return True
    return False

total = 0
for x in xrange(1, limit + 1):
    if not sum_of_two_abs(x):
        total += x

print total
