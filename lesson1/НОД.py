a = int(input())
b = int(input())
max_del = 1
for i in range(1, max(a,b)):
    if a%i == 0 and b%i == 0:
        if i > max_del:
            max_del = i
print(max_del)

