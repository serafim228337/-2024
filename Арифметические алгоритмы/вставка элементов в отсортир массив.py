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
        return mid + 1


sorted_array = [1, 3, 5, 7, 9]
new_el = 6
mest = binary_search(sorted_array, new_el) + 1
sorted_array.insert(mest, new_el)
print(sorted_array)
