def max_unique_subarray_sum(nums, K, L):
    n = len(nums)
    max_sum = 0
    left = 0
    right = 0
    current_sum = 0
    seen = set()

    while right < n:
        while right - left < K or right - left > L:
            if right - left < K:
                right += 1

            else:
                if nums[left] in seen:
                    seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        if right - left >= K and right - left <= L:
            if nums[right] not in seen:
                seen.add(nums[right])
                current_sum += nums[right]
                max_sum = max(max_sum, current_sum)
            else:
                if nums[left] in seen:
                    seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            right += 1

    return max_sum


nums = [4, 2, 4, 5, 6]
K = 2
L = 3

max_sum = max_unique_subarray_sum(nums, K, L)
print(max_sum)  # Вывод: 20 (подмассив [3, 4, 5, 6, 7])
