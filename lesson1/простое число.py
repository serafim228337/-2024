for a in range(n):
    prost_chisl = []
    col = 0
    for i in range(1, a + 1):
        if a % i == 0:
            col += 1
        if col > 2:
            break
        if a == 1:
            break
    else:
        prost_chisl.append(a)
