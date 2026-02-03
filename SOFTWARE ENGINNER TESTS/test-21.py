#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

def countIsolatedCommunicationGroups(links, n):
    # Write your code here
    pass

def count_components(n, links):
    graph = [[] for _ in range(n + 1)]

    for a, b in links:
        graph[a].append(b)
        graph[b].append(a)

    print(graph)

    visited = [False] * n
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)


if __name__ == '__main__':

    n = 4

    links = [
        #random non sorted links
        [0, 1], # [1], [0]
        [1, 2],  # [0, 2], [1]
        [2, 3],  # [1, 3], [2]
        [3, 4]   # [2, 4], [3]
    ]

    count_components(n, links)
