
n = int(input())
w = []
for i in range(n):
    row = [int(x) for x in input().split()]
    w.append(row)
    
for row in w:
    for x in row:
        print(f"{x:2}",end="")
    print()