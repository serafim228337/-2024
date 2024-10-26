def result_dict(text):
    slov = {}
    for i in text:
        slov[i] = text.count(i)
    return slov


def compressed(text):
    slov = {}
    spis = []
    answ = ""
    for i in text:
        spis.append(i)
        slov[i] = text.count(i)
    for i in range(len(spis)):
        answ += str(slov[spis[i]])
    return answ


print(result_dict("apple"))
print(compressed("apple"))
