def balance(s):
    count = 0
    for char in s:
        if char == "+":
            count += 1
        elif char == "-":
            count -= 1
    return count
print(balance("++-+"))