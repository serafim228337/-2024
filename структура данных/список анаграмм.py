def group_anagreams(world_list):
    answ = []
    spis = []
    words = []
    dict = {}
    for word in world_list:
        for i in word:
            words.append(i)
        words.sort()
        a = "".join(words)
        if a not in dict:
            dict[a] = [word]
        else:
            dict[a].append(word)
        spis.append(a)
        words.clear()
    for key in dict:
        answ.append(dict[key])
    return answ


spis_slov = ["tea", "eat", "top"]
group_anagreams(spis_slov)
print(group_anagreams(spis_slov))
