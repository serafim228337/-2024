def max_subsequence_length(arr, k):
  max_length = 0
  current_sum = 0
  start = 0

  for i in range(len(arr)):
    current_sum += arr[i]

    while current_sum > k:
      current_sum -= arr[start]
      start += 1

    max_length = max(max_length, i - start + 1)

  return max_length

arr = [1, 4, 2, 10, 2, 3, 1, 5]
k = 7

max_length = max_subsequence_length(arr, k)
print(max_length)