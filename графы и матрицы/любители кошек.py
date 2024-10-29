def count_triangles(n, m, edges):

    adjacency_list = [[] for _ in range(n + 1)]
    for a, b in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    count = 0
    for i in range(1, n + 1):
        for j in adjacency_list[i]:
            for k in adjacency_list[j]:
                if k == i and k > j:
                    count += 1
                    break

    return count // 3


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

print(count_triangles(n, m, edges))
