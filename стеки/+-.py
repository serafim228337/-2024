def operacii(s):
    count = 0
    for i in s:
        if i == "+":
            count += 1
        elif i == "-":
            count = max(0, count - 1)
    return(count)
print(operacii("++-----"))