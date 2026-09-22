# Take number of vertices and edges from the user
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: u v weight")

# Take all edges as input
for _ in range(m):

    while True:
        edge = input().strip()

        if edge:
            u, v, w = map(int, edge.split())
            break

    edges.append((w, u, v))


# Sort edges according to weight
edges.sort()


# Parent array for Disjoint Set
parent = list(range(n))

# Rank array for optimizing union operation
rank = [0] * n


# Find the parent of a vertex
def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


# Join two sets
def union(a, b):

    rootA = find(a)
    rootB = find(b)

    # Already connected
    if rootA == rootB:
        return False

    # Attach smaller rank tree to larger rank tree
    if rank[rootA] < rank[rootB]:
        parent[rootA] = rootB

    elif rank[rootA] > rank[rootB]:
        parent[rootB] = rootA

    else:
        parent[rootB] = rootA
        rank[rootA] += 1

    return True


# Store edges selected for MST
mst = []

# Store total cost
totalCost = 0


# Process edges in increasing order of weight
for weight, u, v in edges:

    # Add edge only if it does not create a cycle
    if union(u, v):

        mst.append((u, v, weight))
        totalCost += weight

        # MST contains n-1 edges
        if len(mst) == n - 1:
            break


# Check if MST exists
if len(mst) != n - 1:

    print("\nMST does not exist because the graph is disconnected.")

else:

    print("\nMinimum Spanning Tree:")

    for u, v, weight in mst:
        print(u, "--", v, "Weight =", weight)

    print("\nMinimum Cost =", totalCost)