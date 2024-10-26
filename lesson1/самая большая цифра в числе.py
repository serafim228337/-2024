def max_chisl(a):
    maxx = -99999999999999
    for i in range(len(a)):
        if int(a[i]) > maxx:
            maxx = int(a[i])
    return maxx
