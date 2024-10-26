def NOD(a, b):
    max_del = 1
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            if i > max_del:
                max_del = i
    return max_del


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2
