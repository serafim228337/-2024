n = int(input())
palochki = []
answ = []
for i in range(1, n + 1):
    a = int(input())
    if a != 0:
        palochki.append([i] * a)
for spis in palochki:
    for numb in spis:
        if numb == 2 or numb == 1:
            answ.append(numb)
        if numb % 2 == 0 and numb != 2:
            answ.append(numb // 2)
            answ.append(numb // 2)
        elif numb % 2 != 0 and numb != 1:
            answ.append(numb // 2)
            answ.append((numb // 2) + 1)

maxx = -9
maxim = []
chisl = set()
for i in answ:
    if answ.count(i) >= maxx:
        maxx = answ.count(i)
        maxim.append(answ.count(i))
        chisl.add(i)
print(maxx)
print(min(chisl))
