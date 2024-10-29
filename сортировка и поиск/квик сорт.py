def quicksort(arr):
    if len(arr) <= 1:
        return arr
    for slov in arr:
        pivot = slov["price"]
        left = [x for x in slov if x < pivot]
        right = [x for x in slov if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


arr = [{"name": "apple", "price": 200}, {"name": "banana", "price": 100}, {"name": "banana", "price": 100}]
sorted_arr = quicksort(arr)
print(sorted_arr)
