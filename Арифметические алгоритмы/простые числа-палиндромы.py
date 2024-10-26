def prost_numb(a):
    col = 0
    for i in range(1, a + 1):
        if a % i == 0:
            col += 1
        if col > 2:
            break
        if a == 1:
            break
    else:
        return True


def palindrom(a):
    a = str(a)
    if len(a) % 2 != 0:
        one = a[:len(a) // 2 + 1]
        two = a[len(a) // 2:]
        if one == two[::-1]:
            return True
        else:
            return False
    else:
        one = a[:len(a) // 2]
        two = a[len(a) // 2:]
        if one == two[::-1]:
            return True
        else:
            return False


def simpleandpalindom(n):
    answ = []
    for i in range(1, n):
        if prost_numb(i) and palindrom(i):
            answ.append(i)
    return (answ)


print(simpleandpalindom(20000))
