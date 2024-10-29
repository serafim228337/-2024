def selection_sort(lst):
    slov = {}
    for i in range(len(lst)):
        big = i

        for j in range(i + 1, len(lst)):
            if lst[j] > lst[big]:
                big = j
        lst[big], lst[i], = lst[i], lst[big],
    for i in lst:
        slov[i] = lst.count(i)
    return slov


# sort a list
L = [99, 9, 0, 2, 1, 0, 1, 100, -2, 8, 7, 4, 3, 2]
print(selection_sort(L))

print("The sorted list is: ", L)
