n = int(input())
string = 0
i = 1
c = 0
while c != n:
    if i % 3 != 0:
        c += 1
        string = i
    i += 2
print(string)
