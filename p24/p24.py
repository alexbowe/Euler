
# Taken from KNUTH AOCP 4A page 319
def next_perm(perm):
    n = len(perm)
    j = n - 1
    
    while perm[j-1] >= perm[j+1-1]:
        if j == 0: break 
        j-=1

    l = n
    while perm[j-1] >= perm[l-1]:
        if l == 0: break
        l-=1

    perm[l-1], perm[j-1] = perm[j-1], perm[l-1]

    k, l = j + 1, n
    while k < l:
        perm[k-1], perm[l-1] = perm[l-1], perm[k-1]
        k += 1
        l -= 1
    
    return perm

def perm_gen(perm):
    while 1:
        yield perm
        perm = next_perm(perm)

def take(n, g):
    while n > 0:
        n-=1
        yield g.next()

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mil = [x for i,x in enumerate(take(1e6, perm_gen(seq))) if i == 1e6 - 1][0]

def to_num(seq):
    n = 0
    for d in seq:
        n = n * 10 + d
    return n

print to_num(mil)
