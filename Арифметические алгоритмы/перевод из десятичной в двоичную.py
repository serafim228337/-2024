def translate(n):
    new_numb = ''
    while n > 0:
        new_numb = str(n % 2) + new_numb
        n = n // 2
    return new_numb


def retranslate(n):
    n = str(n)
    n_r = n[::-1]
    new_numb = ''
    print(n, n_r)
    for i in range(len(n)):
        print(str(int(n[i]) * int(n_r[i])))
        new_numb += str(int(n[i]) * int(n_r[i]))
    return new_numb


print(translate(10))
print(retranslate(1010))
