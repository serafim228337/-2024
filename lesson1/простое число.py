def prost_numb(a):
    col = 0
    for i in range(1, a + 1):
        if a % i == 0:
            col += 1
        if col > 2:
            return ("NO")
            break
        if a == 1:
            return ("NO")
            break
    else:
        return ("Yes")


print(prost_numb(2))
print(prost_numb(5))
print(prost_numb(6))
