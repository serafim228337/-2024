a = input()
if len(a) % 2 != 0:
    one = a[:len(a) // 2 + 1]
    two = a[len(a) // 2:]
    if one == two[::-1]:
        print("YES")
    else:
        print("NO")
else:
    one = a[:len(a) // 2]
    two = a[len(a) // 2:]
    if one == two[::-1]:
        print("YES")
    else:
        print("NO")
