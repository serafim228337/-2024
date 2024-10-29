n = int(input())
dict = {}
for i in range(2, n + 1):
    a = int(input())
    if a not in dict:
        dict[a] = [i]
    else:
        dict[a].append(i)
if len(dict) != 0:
    maxim = max(dict)
    print(maxim)
    print(len(dict[maxim]))
    print(*dict[maxim])
