def merge_sorted_arrays(array1, array2):
    merged_array = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            merged_array.append(array2[j])
            j += 1
        else:
            merged_array.append(array1[i])
            merged_array.append(array2[j])
            i += 1
            j += 1

    while i < len(array1):
        merged_array.append(array1[i])
        i += 1
    while j < len(array2):
        merged_array.append(array2[j])
        j += 1

    return merged_array


array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8, 10]

merged_array = merge_sorted_arrays(array1, array2)
print(merged_array)
