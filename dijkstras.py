import heapq

# Take number of vertices and edges from the user
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

# Create adjacency list
graph = [[] for _ in range(n)]

print("Enter edges as: u v weight")

# Take all edges as input
for _ in range(m):

    # Keep asking until a non-empty input is given
    while True:
        edge = input().strip()

        if edge:
            u, v, w = map(int, edge.split())
            break

    # Add edge in both directions because graph is undirected
    graph[u].append((v, w))
    graph[v].append((u, w))

# Take source vertex
source = int(input("Enter source vertex: "))

# Initially, distance of every vertex is infinity
dist = [float('inf')] * n

# Distance from source to itself is 0
dist[source] = 0

# Priority queue stores (distance, vertex)
pq = [(0, source)]

# Dijkstra's algorithm
while pq:

    # Get vertex with minimum distance
    d, node = heapq.heappop(pq)

    # Ignore outdated entries
    if d > dist[node]:
        continue

    # Check all adjacent vertices
    for neighbor, weight in graph[node]:

        # Calculate new distance
        newDist = d + weight

        # If new distance is smaller, update it
        if newDist < dist[neighbor]:
            dist[neighbor] = newDist

            # Add updated distance to priority queue
            heapq.heappush(pq, (newDist, neighbor))

# Display shortest distances
print("\nShortest distances from source", source)

for i in range(n):

    if dist[i] == float('inf'):
        print(i, "-> INF")
    else:
        print(i, "->", dist[i])