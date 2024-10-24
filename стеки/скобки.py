def balance(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0


print(balance("()"))
