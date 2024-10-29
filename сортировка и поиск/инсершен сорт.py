def insertionSort(arr):
    n = len(arr)
    slov = {}
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    for i in arr:
        if i[0] not in slov:
            slov[i[0]] = 1
        else:
            slov[i[0]] += 1
    print(slov)


# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = ["Alice", "Charlie", "Bob", "Eve", "David", "Charlie", "Bob"]
insertionSort(arr)
print(arr)