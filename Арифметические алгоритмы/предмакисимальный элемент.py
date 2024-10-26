def pred_max(spis):
    maxx = -99999999999999
    answ = -99999999
    for i in spis:
        if answ < i < maxx:
            answ = i
        if i > maxx:
            maxx = i
    return answ


spis = [36, 36, 9]
print(pred_max(spis))
