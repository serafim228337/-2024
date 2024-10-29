n, m, v = map(int, input().split())
cort = set()
spis = set()
cort.add(v)
for i in range(m):
    u, v = map(int, input().split())
    if u in cort:
        cort.add(v)
        spis.add(u)
spis.add(v)

print(len(cort))
print(*spis)