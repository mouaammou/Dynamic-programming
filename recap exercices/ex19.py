

def countIsolatedCommunicationGroups(links, n):
    # build undirected graph
    graph = {i: [] for i in range(n)}
    for a, b in links:
        graph[a].append(b)
        graph[b].append(a)

    print(graph)
    # return
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    groups = 0
    for node in range(n):
        if node not in visited:
            dfs(node)
            groups += 1

    return groups

def countIsolatedCommunicationGroups(links, n):
    parent = list(range(n))      # each node is its own parent
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return 0              # already same component
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra           # merge smaller into larger
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return 1                  # merged two components

    components = n
    for a, b in links:
        components -= union(a, b)

    return components


if __name__ == '__main__':
    n = 6
    links = [[0, 1], [1, 3], [4, 5]]
    result = countIsolatedCommunicationGroups(links, n)
    print(result)  # => 3