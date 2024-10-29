def merge_sort(nums):
    summ = 0
    c = 0
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i]['price'] < right[j]['price']:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return nums


def sredn(spis):
    summ = 0
    c = 0
    for slov in spis:
        summ += slov['price']
        c += 1
    return summ / c


a = [{"name": "apple", "price": 200}, {"name": "banana", "price": 150}, {"name": "banana", "price": 100},
     {"name": "banana", "price": 150}]
print(merge_sort(a))
print(sredn(a))
