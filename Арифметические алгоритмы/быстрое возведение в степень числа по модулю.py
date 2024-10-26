def stepen_mod(a, b, m):
    if b % 2 == 0:
        answ = ((a ** (b / 2) % m) ** 2) % m
    else:
        answ = a * (a ** (b - 1) % m) % m
    return answ


print(stepen_mod(123, 65537, 9871))
