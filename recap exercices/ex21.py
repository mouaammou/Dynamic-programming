

# def verifySameMultisetDifferentStructure(root1, root2):
    
#     values1 = [x for x in root1 if x != 100001]
#     values2 = [x for x in root2 if x != 100001]
    
#     if sorted(values1) != sorted(values2):
#         return False

#     values1 = [1 if x != 100001 else 0 for x in root1]
#     values2 = [1 if x != 100001 else 0 for x in root2]

#     print(values1)
#     print(values2)

#     if values1 == values2:
#         return False
#     return True


def verifySameMultisetDifferentStructure(root1, root2):
    
    # Step 1: Extract values from both trees (ignore nulls)
    def get_values(node, values):
        if node == 100001 or node is None:
            return
        values.append(node)
    
    # Step 2: Get structure signature using DFS
    def get_structure(node, nodes, i=0):
        if i >= len(nodes) or nodes[i] == 100001:
            return "N"
        left = get_structure(node, nodes, 2*i+1)
        right = get_structure(node, nodes, 2*i+2)
        return f"({left},{nodes[i]},{right})"
    
    # Check same values
    values1, values2 = [], []
    for v in root1:
        get_values(v, values1)
    for v in root2:
        get_values(v, values2)
    
    if sorted(values1) != sorted(values2):
        return False
    
    # Check different structure
    struct1 = get_structure(None, root1)
    struct2 = get_structure(None, root2)
    
    # print(struct1)
    # print(struct2)

    return struct1 != struct2


if __name__ == '__main__':
    root1 = [4, 2, 6, 1, 3, 5, 7]
    root2 = [4, 2, 6, 1, 3, 7, 5]

    result = verifySameMultisetDifferentStructure(root1, root2)

    print((result))