a = input()
answ = ""
for i in range(len(a)):
    if int(a[i]) % 2 != 0:
        answ += a[i]
print(answ)
