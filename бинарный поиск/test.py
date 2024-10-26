def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
print(binary_search([0, 5, 3, 4, 9, 3, -2]))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9]))