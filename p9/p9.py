import math

for a in range(1, 500):
    for b in range(a+1, 1000):
        c = math.sqrt(a*a + b*b)
        if (a + b + c) == 1000:
            print a, b, int(c)
            print a*b*int(c)
