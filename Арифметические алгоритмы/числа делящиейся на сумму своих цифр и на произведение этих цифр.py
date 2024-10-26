def check(numb):
    suma = 0
    mult = 1
    answ = []
    for n in range(1, numb):
        num = n
        while n > 0:
            digit = n % 10
            suma += digit
            mult *= digit
            n //= 10
        print(num, suma, mult)
        if mult != 0 and num % suma == 0 and num % mult == 0:
            answ.append(num)
        suma = 0
        mult = 1
    return answ


print(check(50))
