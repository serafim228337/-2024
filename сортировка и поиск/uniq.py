def sortt(a):
    slov = {}
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j].lower() > a[j + 1].lower():
                a[j], a[j + 1] = a[j + 1].lower(), a[j].lower()
    print(a)
    for i in a:
        slov[i] = a.count(i)
    return slov


mas = ["a", 'a', 'b', 'a', 'A']
print(sortt(mas))
