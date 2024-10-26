def fibb(n):
    f1 = 1
    f2 = 1
    i = 0
    while i < n - 2:
        sum_f = f1 + f2
        f1 = f2
        f2 = sum_f
        i += 1
    return f2


print(fibb(10))
