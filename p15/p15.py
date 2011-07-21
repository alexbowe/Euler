def count(n, row=0, col=0):
    ans = 0

    if row == n and col == n:
        return 1
    if row > n or col > n:
        return 0

    ans += count(n, row, col+1)
    ans += count(n, row+1, col)

    return ans

# central binomial coefficients
def pascal_row(n):
    """Returns a generator for the nth row of pascal's triangle"""
    # Which side of pascal's triangle is the kth position on?
    v = 1
    yield v
    for i in range(0, n):
        v = ((n - i) * v) / (i+1)
        yield v

def count2(n):
    pasc = list(pascal_row(2*n))
    return pasc[n]


n = 20
print count2(n)

