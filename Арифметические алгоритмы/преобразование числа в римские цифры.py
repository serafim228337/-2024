def translate(n):
    answ = ""
    val = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    syms = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while n:
        div = n // val[i]
        n %= val[i]

        while div:
            answ += syms[i] + ""
            div -= 1
        i -= 1
    return answ
print(translate(1994))


