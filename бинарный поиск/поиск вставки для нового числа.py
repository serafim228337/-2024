def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    if target < arr[low]:
        return 0
    elif target > arr[high]:
        return high + 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    if target < arr[mid]:
        return mid - 1
    else:
        return  mid + 1


print(binary_search([1, 3, 4, 5, 8, 9], 6))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(binary_search([-5, -4, -3, -2], 6))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], -5))