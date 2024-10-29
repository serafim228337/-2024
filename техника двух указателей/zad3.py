def closestPairSum(arr, target):
    n = len(arr)
    res = []
    minDiff = float('inf')

    left = 0
    right = n - 1

    while left < right:
        currSum = arr[left] + arr[right]
        if abs(target - currSum) < minDiff:
            minDiff = abs(target - currSum)
            res = [arr[left], arr[right]]

        if currSum < target:
            left += 1

        elif currSum > target:
            right -= 1

        else:
            return res
    return res


arr = [10, 22, 28, 29, 30, 40]
target = 54
res = closestPairSum(arr, target)
if len(res) > 0:
    print(res[0], res[1])
