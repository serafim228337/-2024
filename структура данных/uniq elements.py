def spis(arr):
    answ = {}
    for i in arr:
        answ[i] = arr.count(i)
    return answ


print(spis(["apple", "pig", "car", "123", "banana", "banana"]))
