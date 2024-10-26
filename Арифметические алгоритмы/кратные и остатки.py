def kratnandost(n, m):
    answ = []
    for i in range(1, m):
        if i % n == 0:
            answ.append(i)
    return sum(answ)


print(kratnandost(3, 20))
