def sortirovka_name(spis):
    dict = {}
    answ = []
    for i in spis:
        if i[0] not in dict:
            dict[i[0]] = i
    print(dict)
    sorted_dict = sorted((dict))
    for a in sorted_dict:
        answ.append(dict[a])
    return answ


def sortirovka_age(spis):
    dict = {}
    answ = []
    for i in spis:
        if i[0] not in dict:
            dict[i[1]] = i
    sorted_dict = sorted((dict))
    for a in sorted_dict:
        answ.append(dict[a])
    return answ


spisok = [["Alice", 30], ["Bob", 25], ["Charliw", 30], ["David", 20], ["Alice", 20]]
print(sortirovka_name(spisok))
print(sortirovka_age(spisok))
