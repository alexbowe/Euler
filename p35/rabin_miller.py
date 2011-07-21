import random

def is_prime_rm(n,k=100):
    if n<2:         return False
    if n==2 or n==3:return True
    if not n%2:     return False

    s = 0 
    d = n-1 
    while True:
        q,r = divmod(d,2)
        if r==1: break
        s+=1;d=q

    def isWitness(a):
        x = pow(a,d,n)
        if x==1 or x==n-1: return False
        for r in range(s):
            x = pow(a,2**r*d,n)
            if x==-1 or x==n-1: return False
        return True

    for i in range(k):
        a = random.randint(2,n-2)
        if isWitness(a): return False
    return True

