chisl = int(input())
a = int(input())
while a != chisl:
    if a < chisl:
        print("Больше")
    if a > chisl:
        print("Меньше")
    a = int(input())
print("Угадал!")
