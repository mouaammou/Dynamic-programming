#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

def count_connected_computers(links, n):
    graph = {i: [] for i in range(n)}

    # print(graph)
    for a, b in links:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    components = 0
    def dfs(start):
        nonlocal components
        visited.add(start)
        # print(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(neighbor)
                components += 1

    dfs(0)
    return components
    

def countIsolatedCommunicationGroups(links, n):
    graph = {i: [] for i in range(n)}
    for a, b in links:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    print(graph)
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    components = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1

    return components



def countIsolatedCommunicationGroups(links, n):
    parent = [i for i in range(n)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    for a, b in links:
        union(a, b)

    # Count unique parents (connected components)
    groups = set(find(i) for i in range(n))
    return len(groups)


if __name__ == '__main__':

    n = 4

    links = [
        [0, 1],
        [1, 2]
    ]

    print(countIsolatedCommunicationGroups(links, n))  # Output: 2
    # count_connected_computers(links, n)