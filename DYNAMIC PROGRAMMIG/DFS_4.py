graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        print("neighbor --> graph[node] --> node: ", neighbor, graph[node], node)
        dfs(neighbor)



count = 0
for node in graph:
    if node not in visited:
        dfs(node)
        print("visited: ", visited)
        count += 1

print(count)