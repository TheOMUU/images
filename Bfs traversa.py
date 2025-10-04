from queue import Queue

# Take graph input from user
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

adj_list = {}

# Initialize adjacency list
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    adj_list[node] = []

print("\nEnter edges (format: U V meaning U → V and V → U):")
for _ in range(m):
    u, v = input().split()
    adj_list[u].append(v)
    adj_list[v].append(u)  # remove this line if graph is directed

print("\nAdjacency List:", adj_list)

# Initialize BFS helpers
visited = {}
level = {}
parent = {}
bfs_traversal = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

# Take source input
source = input("\nEnter source node: ")
visited[source] = True
level[source] = 0
queue.put(source)

# BFS Traversal
while not queue.empty():
    u = queue.get()
    bfs_traversal.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

print("\nBFS traversal:", bfs_traversal)

# Shortest Path
target = input("Enter target node: ")
path = []

while target is not None:
    path.append(target)
    target = parent[target]

path.reverse()
print("Shortest path is:", path)
