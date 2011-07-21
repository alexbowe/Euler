def digit_gen(n):
    while n > 0:
        yield n % 10
        n /= 10

print sum(digit_gen(2**1000))
