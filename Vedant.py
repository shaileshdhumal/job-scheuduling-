# Kruskal's Algorithm

edges = [
    (1, 'A', 'B'),
    (2, 'B', 'C'),
    (3, 'A', 'C'),
    (4, 'B', 'D')
]

edges.sort()

parent = {}

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    parent[find(x)] = find(y)

# vertices
for v in ['A', 'B', 'C', 'D']:
    parent[v] = v

cost = 0

print("MST:")

for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, "=", w)
        cost += w

print("Total Cost =", cost)
