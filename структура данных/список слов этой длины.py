def spis(arr):
    answ = {}
    for i in arr:
        if len(i) not in answ:
            answ[len(i)] = [i]
        else:
            answ[len(i)].append((i))
    return answ


print(spis(["apple", "pig", "car", "123", "banana"]))
