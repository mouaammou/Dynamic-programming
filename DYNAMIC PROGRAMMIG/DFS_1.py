#  EXERCISE 1: DFS on a TREE (print all nodes)
#  Problem

# You are given a tree represented as a dictionary.
# Print all nodes using DFS starting from "A".

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

def dfs(node):
    print(node)

    for child in tree[node]:
        dfs(child)

dfs("A")