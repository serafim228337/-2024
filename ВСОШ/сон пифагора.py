n = int(input())
c = 0
a = 1

while n > 0:
    c += 1
    if (n % (pow(10, a))) == 0:
        b = (n % (pow(10, a))) // (pow(10, a - 1))
        while b == 0:
            a += 1
            b = (n % (pow(10, a))) // (pow(10, a - 1))
    else:
        a = 1
        b = (n % (pow(10, a)))
    n -= b

print(c)
