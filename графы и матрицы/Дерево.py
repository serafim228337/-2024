n, m = map(int, input().split())
spis_ot = []
spis_do = []
for i in range(m):
    ot, do = map(int, input().split())
    spis_ot.append(ot)
    spis_do.append(do)
for i in range(len(spis_ot)):
    if spis_do[i] in spis_ot:
        print("NO")
        break
else:
    print("YES")