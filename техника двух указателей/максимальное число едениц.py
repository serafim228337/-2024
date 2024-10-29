def max_ones_with_one_zero_flip(arr):
    left = 0
    right = 0
    max_length = 0
    zero_count = 0

    while right < len(arr):
        if arr[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if arr[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


arr = [1, 0, 1, 0, 1]
result = max_ones_with_one_zero_flip(arr)
print(result)  # 3
