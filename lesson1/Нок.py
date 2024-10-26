def NOK(a, b, d):
    c = 1
    while True:
        if c % a == 0 and c % b == 0 and c % d == 0:
            break
        c += 1
    return c


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def nok(a, b):
    return (a * b) / gcd_rem_division(a, b)


print(NOK(6, 8, 12))
