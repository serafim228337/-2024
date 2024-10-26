N = int(input())
W = []

for i in range(N):
    row = [int(x) for x in input().split()]
    W.append(row)

print(W)
INF = 30000
selected = [False] * N
dist = [INF] * N
minDist = 0
start = 0
dist[start] = 0
V = start

while minDist < INF:
    selected[V] = True
    for i in range(N):
        if dist[V] + W[V][i] < dist[i] and W[V][i] != 0:
            dist[i] = dist[V] + W[V][i]
    minDist = INF
    for i in range(N):
        if not selected[i] and dist[i] < minDist:
            minDist = dist[i]
            V = i
V = N - 1
print(dist[V])
while V != start:
    for i in range(N):
        if i != V and dist[i] + W[i][V] == dist[V]:
            V = i
            break
    print(V)
