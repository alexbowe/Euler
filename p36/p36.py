import math

def get_digit(i, n):
    return n / 10**i % 10

def get_bit(i, n):
    return (n & (1 << i)) >> i

def num_len(base,n):
    return int(math.log(n,base)) + 1

def is_palindrome(get_i, base, n):
    l = num_len(base, n)
    
    for i in range(l/2):
        if get_i(i, n) is not get_i(l - 1 - i, n):
            return False
    return True

def palin_2(n):
    return is_palindrome(get_bit, 2, n)

def palin_10(n):
    return is_palindrome(get_digit, 10, n)

print sum(filter(lambda x: palin_2(x) and palin_10(x), range(1,10**6)))
