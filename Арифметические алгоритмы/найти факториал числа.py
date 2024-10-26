def factorial(numb):
    for i in range(1, numb):
        numb *= i
    return numb


def fact(numb):
    if numb == 1:
        return numb
    return fact(numb - 1) * numb


print(fact(100))
print(factorial(100))
