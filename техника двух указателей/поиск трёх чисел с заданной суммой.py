def find_triplet(arr, S):
    n = len(arr)
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            summ = arr[i] + arr[left] + arr[right]
            if summ == S:
                return [arr[i], arr[left], arr[right]]
            elif summ < S:
                left += 1
            else:
                right -= 1

    return None


arr = [-1, 0, 1, 2, -1, -4]
S = 0

result = find_triplet(arr, S)
print(result)
