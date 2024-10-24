def check(s):
    stack1 = []
    spis = []
    stack2 = []
    stack3 = []
    flag = False
    word = ""
    for i in s:
        if i == "<":
            stack1.append(i)
            flag = True
        elif i == ">":
            flag = False
            if len(stack1) == 0:
                return False
            else:
                stack1.pop()
        if flag and i != "<":
            word += i
        if len(word) != 0 and not flag:
            spis.append(word)
            word = ""
    for a in spis:
        if a[0] != "/":
            stack2.append(1)
            stack3.append(a)
        else:
            if len(stack3) != 0:
                if a[1:] == stack3[-1]:
                    stack3.pop()
                else:
                    return False
            if len(stack2) == 0:
                return False
            else:
                stack2.pop()
    return len(stack1) == 0 and len(stack2) == 0

print(check('<dev></dev>'))
print(check('<dev><p></p></dev>'))
print(check("<dev><p></dev></p>"))