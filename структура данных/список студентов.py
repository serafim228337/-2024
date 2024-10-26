def sortt(arr):
    sorted_list = sorted(arr, key=lambda x: x['grade'])
    sorted_list = [{'name': entry['name'], 'grade': entry['grade']} for entry in sorted_list]
    return sorted_list


spis = [
    {"name": 'Alice', 'grade': 85},
    {"name": 'Bob', 'grade': 76},
    {"name": 'A', 'grade': 76}
]

list_of_dicts = [{'name': 'Alice', 'grade': 25}, {'name': 'Bob', 'grade': 30}, {'name': 'Charlie', 'grade': 22}]
print(sortt(spis))
print(sortt(list_of_dicts))
