def is_triangle(x):
    # x = 0.5 n (n + 1)
    # 2x = n ( n + 1)
    # n^2 + n - 2x = 0
    from math import sqrt
    n = 0.5 * (-1 + sqrt(1 + 8*x))
    return n == int(n)

def num_value(c):
    return ord(c) - ord('A') + 1

def is_triangle_word(word):
    return is_triangle(sum(map(num_value, word)))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print 'specify file!'
        exit()
    elif len(sys.argv) > 2:
        print 'too many arguments'
        exit()

    file_name = sys.argv[1]
    with open(file_name, 'r') as f:
        words = [w.lstrip('"').rstrip('"') for w in f.read().split(',')]
    
    counter = lambda c,w: (c+1) if is_triangle_word(w) else c
    print reduce(counter, words, 0)
