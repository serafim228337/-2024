n, m = map(int, input().split())
cort = set()
spis = []
new_spis = []

u, v = map(int, input().split())
spis.append(u)
spis.append(v)

for i in range(m - 1):
    u, v = map(int, input().split())
    if u in spis or v in spis:
        spis.append(u)
        spis.append(v)
    else:
        new_spis.append(u)
        new_spis.append(v)
    if (u in new_spis or v in new_spis) and u in spis or v in spis:
        for a in new_spis:
            spis.append(a)

cort = set(spis)

if len(cort) == n:
    print("YES")
else:
    print("NO")
