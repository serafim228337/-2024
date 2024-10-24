a = input()
col = 0
while a != "Приехали!":
    if "зайка" in a:
        col += 1
    a = input()
print(col)
