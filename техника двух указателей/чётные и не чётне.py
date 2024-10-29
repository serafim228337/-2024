def partition_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1

        while left < right and arr[right] % 2 != 0:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


arr = [1, 4, 2, 3, 5, 8, 7]

partitioned_arr = partition_array(arr)
print(partitioned_arr)
