def is_perfect(n):
    sum_divisors = 0
    answ = []
    spis = [i for i in range(n)]
    for number in spis:
        for i in range(1, number):
            if number % i == 0:
                sum_divisors = sum_divisors + i
        if sum_divisors == number:
            answ.append(number)
    return answ

print(is_perfect(30))