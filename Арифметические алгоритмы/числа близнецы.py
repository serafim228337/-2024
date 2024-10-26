def blizneci(N):
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0]
    answ = []

    for i in range(len(primes) - 1):
        if (primes[i + 1] - primes[i]) == 2:
            answ.append((primes[i], primes[i + 1]))
    return answ


print(blizneci(20))
