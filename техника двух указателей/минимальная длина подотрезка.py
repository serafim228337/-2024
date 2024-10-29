def min_subsequence_length(arr, S):
    min_length = float('inf')
    current_sum = 0
    start = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        while current_sum >= S:
            if start != i:
                min_length = min(min_length, i - start + 1)
            current_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0
    else:
        return min_length


arr = [1, 4, 2, 3, 1, 5, 3]
S = 7

min_length = min_subsequence_length(arr, S)
print(min_length)  # 5,3


