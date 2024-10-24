a = int(input())
b = int(input())
c = 1
while True:
    if c % a == 0 and c % b == 0:
        break
    c += 1
print(c)
