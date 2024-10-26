n = int(input())
if n % 2 == 0:
    dlina = n // 2
    shirina = n // 2
    print(dlina * shirina)
else:
    dlina = n // 2 + 1
    shirina = n // 2 + 1
    print(dlina * shirina)