def uniq(a):
    a = a.lower()
    spis = set()
    word = ""
    for i in range(len(a)):
        if a[i].isalpha():
            word += a[i]
        if a[i].isspace() or i == len(a) - 1:
            spis.add(word)
            word = ""
    return spis


print(uniq("word, Word, aaaaa"))
print(uniq("Hello, world! Hello everyone"))
