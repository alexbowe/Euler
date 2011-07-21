def of_form_2n5m(d):
    n, m = 0, 0
    i = 1
    while (d / 2.0) % 5 != 0:
        pass

i, j = 0, 0
while True:
    while True:
        n = 2**i * 5**j
        if n >= 10: break
        print n
        j+=1
    i+=1
