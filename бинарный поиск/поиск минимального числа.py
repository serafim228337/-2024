def binary_search(arr):
    low = 0
    high = len(arr) - 1
    pred = arr[0]
    if arr[high] > arr[low]:
        return arr[low]
    else:
        for i in range(1, len(arr)):
            if arr[i] < pred:
                return (arr[i])

print(binary_search([4, 5, 6, 7, 8, 0 , 1, 2]))
print(binary_search([4, 5, 6, -1, 1, 2]))
print(binary_search([0, 1, 2, 3, 4, 5]))
