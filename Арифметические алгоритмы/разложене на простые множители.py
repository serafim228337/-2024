def razl(n):
    i = 2
    answ = []
    while i * i <= n:
        while n % i == 0:
            answ.append(str(i))
            n //= i
        i += 1
    if n > 1:
        answ.append(str(n))
    return (" * ".join(answ))


print(razl(20))
