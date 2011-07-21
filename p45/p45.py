from numclasses import *

# chosen as it has the greatest stride
def hex_gen(n):
    while 1:
        yield n*(2*n-1)
        n+=1

def find_next_from_hex(n):
    for h in hex_gen(n+1):
        if is_triangle(h) and is_pentagonal(h):
            yield h

if __name__ == '__main__':
    g = find_next_from_hex(143)
    print g.next()
