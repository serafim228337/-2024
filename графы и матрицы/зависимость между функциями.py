n = int(input())
d = {}
svobod = []
lis = []
answ = []
for i in range(n):
    a = input().split()
    lis.append(a[0])
    if len(a) > 1:
        if int(a[1]) not in d:
            d[int(a[1])] = [a[0]]
        else:
            d[int(a[1])].append(a[0])
    else:
        svobod.append(a[0])
for key in d:
    if lis[key] in svobod:
        answ.append(lis[key])
        d[key].sort()
        for a in d[key]:
            answ.append(a)
for key in d:
    if lis[key] not in answ:
        answ.append(lis[key])
        d[key].sort()
        for a in d[key]:
            answ.append(a)
    else:
        d[key].sort()
        for a in d[key]:
            if a not in answ:
                answ.append(a)
for i in svobod:
    if i not in answ:
        answ.append(i)

for i in answ:
    print(i)
