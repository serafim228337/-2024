def NOK(a, b, d):
    c = 1
    while True:
        if c % a == 0 and c % b == 0 and c % d == 0:
            break
        c += 1
    return c


print(NOK(6, 8, 12))
