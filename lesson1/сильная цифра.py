a = input()
maxx = -99999999999999
for i in range(len(a)):
    if int(a[i]) > maxx:
        maxx = int(a[i])
print(maxx)
