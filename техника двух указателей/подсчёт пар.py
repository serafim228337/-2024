def count_unique_pairs(arr, S):
    arr.sort()
    n = len(arr)
    count = 0
    seen = set()

    left = 0
    right = n - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == S:
            pair = tuple(sorted((arr[left], arr[right])))
            if pair not in seen:
                seen.add(pair)
                count += 1

            left += 1
            right -= 1
        elif sum < S:
            left += 1
        else:
            right -= 1

    return count


arr = [1, 2, 3, 4, 5, 6]
S = 7
arr2 = [1, 5, 7, -1, 5]
ss = 6
result = count_unique_pairs(arr, S)
print(result)
print(count_unique_pairs(arr2, ss))
