import heapq

# Take number of vertices and edges from the user
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

# Create adjacency list
graph = [[] for _ in range(n)]

print("Enter edges as: u v weight")

# Take all edges as input
for _ in range(m):

    # Avoid empty input
    while True:
        edge = input().strip()

        if edge:
            u, v, w = map(int, edge.split())
            break

    # Add edge in both directions
    graph[u].append((v, w))
    graph[v].append((u, w))

# Array to keep track of visited vertices
visited = [False] * n

# Priority queue stores (weight, vertex)
pq = [(0, 0)]

totalCost = 0
mst = []

# Prim's algorithm
while pq:

    # Get edge with minimum weight
    weight, node = heapq.heappop(pq)

    # Skip if vertex is already visited
    if visited[node]:
        continue

    # Mark vertex as visited
    visited[node] = True

    # Add edge weight to total cost
    totalCost += weight

    # Store the selected vertex and edge weight
    mst.append((node, weight))

    # Check all adjacent vertices
    for neighbor, edgeWeight in graph[node]:

        # Add unvisited vertices to priority queue
        if not visited[neighbor]:
            heapq.heappush(pq, (edgeWeight, neighbor))

# Check whether MST exists
if len(mst) != n:
    print("\nMST does not exist because the graph is disconnected.")
else:
    print("\nMinimum Spanning Tree:")

    for node, weight in mst:
        print("Vertex:", node, "Edge Weight:", weight)

    print("\nMinimum Cost =", totalCost)