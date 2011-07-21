def diagonal_gen():
    v = 1
    yield v
    step = 2
    while 1:
        for _ in range(4):
            v += step
            yield v
        step += 2

def take(n, it):
    for i in range(n):
        yield it.next()

n = 1001
num = n * 2 - 1
print sum([x for x in take(num, diagonal_gen())])
