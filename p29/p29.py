a_list = range(2, 101)
b_list = range(2, 101)

s = set()

for a in a_list:
    result = a
    for _ in b_list:
        result *= a
        s.add(result)

print len(s)
