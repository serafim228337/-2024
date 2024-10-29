def sortt(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

mas = [1,5,87,34,4323,112,2121,212,-8]
print(sortt(mas))