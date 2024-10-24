x = 0
y = 0
a = input()
while a != "СТОП":
    shag = int(input())
    if a == "СЕВЕР":
        y += shag
    elif a == "ВОСТОК":
        x += shag
    elif a == "ЮГ":
        y -= shag
    elif a == "ЗАПАД":
        x -= shag
    a = input()
print(x)
print(y)
