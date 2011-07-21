import math
k = 3

def num_digits(n):
    return int(math.log(n,10)) + 1

upper = (10**k - 1)**2
lower = 10**(2*(k-1))

lo_size = num_digits(lower)
hi_size = num_digits(upper)
print lo_size, hi_size

# (100a + 10b + c)(100x + 10y + z)
# 10000ax + 1000(bx + ay) + 100(az + cx + by) + 10(cy + bz) + cz
#    A            B        C                 D        E
#  cz = 9 -> c z = 1/9, 3/3, 7/7
# the first two digits (a and x) must be 9 as well (no proof here, but tis will give a
# bigger number if possible

# abccba -> 100001a + 10010b + 1100c
# 11 (9091 a + 910 b + 100 c) (factored)

#[x for x in range(900, 1000) if x%11 == 0]
#[902, 913, 924, 935, 946, 957, 968, 979, 990]
# must have a 1, 3, 7, or 9 as last digit: [913, 957, 979]

# for abc = 913, 957, 979:
# both start with 9, so each one has 900:
# (900 + 10 + 3)(900 + 10x + 3)
# (900 + 50 + 7)(900 + 10x + 7)
# (900 + 70 + 9)(900 + 10x + 1)

def get_digit(i, n):
    return n / 10**i % 10

def is_palindrome(n):
    l = num_digits(n)
    
    for i in range(l/2):
        if get_digit(i, n) is not get_digit(l - 1 - i, n):
            return False
    return True

import heapq
def gen_table():
    d = []
    nums = range(100, 999 + 1)
    for x in nums:
        for y in nums:
            ans = x * y
            if is_palindrome(ans):
                heapq.heappush(d, ans)

    return d

print heapq.nlargest(1, gen_table())[0]
