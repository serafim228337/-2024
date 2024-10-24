s = input()
numb = 0
a = ""
new_s = []
deistv = '+-/*'
for i in range(len(s)):
    if s[i] not in deistv:
        a += s[i]
    else:
        new_s.append(a)
        new_s.append(s[i])
        a = ""

new_s.append(a)
i = 0
while len(new_s) != 1:
    if "*" in new_s or "/" in new_s:
        if new_s[i] == "*":
            new_s[i] = int(new_s[i - 1]) * int(new_s[i + 1])
            new_s.pop(i - 1)
            new_s.pop(i)
            i -= 3
        elif new_s[i] == "/":
            new_s[i] = int(new_s[i - 1]) / int(new_s[i + 1])
            new_s.pop(i - 1)
            new_s.pop(i)
            i -= 3
    else:
        if new_s[i] == "+":
            new_s[i] = int(new_s[i - 1]) + int(new_s[i + 1])
            new_s.pop(i - 1)
            new_s.pop(i)
            i -= 1
        elif new_s[i] == "-":
            new_s[i] = int(new_s[i - 1]) - int(new_s[i + 1])
            new_s.pop(i - 1)
            new_s.pop(i)
            i -= 1
    i += 1

print(*new_s)
