
def hasCircularDependency(n, dependencies):
    graph = [[] for _ in range(n)]
    for u, v in dependencies:
        graph[u].append(v)
    
    visited = [0] * n
    
    def dfs(node):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        
        visited[node] = 1
        for child in graph[node]:
            if dfs(child):
                return True
        visited[node] = 2
        return False
    
    for i in range(n):
        if dfs(i):
            return True
    return False
    
    
if __name__ == '__main__':
    n = 4

    dependencies = [[1, 0], [2, 3], [1, 2]]

    result = hasCircularDependency(n, dependencies)

    print((result))