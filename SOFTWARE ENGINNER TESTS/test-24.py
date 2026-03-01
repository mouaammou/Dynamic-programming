#
# Complete the 'hasCircularDependency' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY dependencies
#

def hasCircularDependency(n, dependencies):
    graph = {i: [] for i in range(n)}
    for i, j in dependencies:
        graph[i].append(j)

    visited = set()
    recycle = set()

    def dfs(node):
        if node in recycle:
            return True
        if node in visited:
            return False

        recycle.add(node)
        for child in graph[node]:
            if dfs(child):
                return True
        recycle.remove(node)
        visited.add(node)
        return False

    for i in range(n):
        if dfs(i):
            return True
    return False

from collections import deque

def hasCircularDependency(n, dependencies):
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n
    for u, v in dependencies:
        graph[u].append(v)
        in_degree[v] += 1


    queue = deque([i for i in range(n) if in_degree[i] == 0])
    visited_count = 0

    print("graph: ", graph)
    print("in_degree: ", in_degree)
    print("queue: ", queue)
    # return 
    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return 0 if visited_count == n else 1

if __name__ == '__main__':
    n = 5
    dependencies = [[0, 2], [2, 3], [3, 2], [4, 0]] 
    result = hasCircularDependency(n, dependencies)
    print(bool(result))