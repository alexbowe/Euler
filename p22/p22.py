def remove_quotes(s):
    return s.lstrip('"').rstrip('"')

def char_value(c):
    return ord(c) - ord('A') + 1

def alpha_value(s):
    total = 0
    for c in s:
        total += char_value(c)
    return total

def score_gen(names):
    for (i, name) in enumerate(names):
        yield (i+1) * alpha_value(name)

if __name__ == '__main__':
    with open('names.txt', 'r') as f:
        names = map(remove_quotes, f.read().split(','))

    names.sort()
    print sum(score_gen(names))
