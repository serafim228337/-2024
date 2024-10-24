a = int(input())
summ = 0
while a != 0:
    if a >= 500:
        a = a * 0.9
    summ += a
    a = int(input())
print(summ)
