from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        old_node = head
        hash_map = {}
        while old_node:
            hash_map[old_node] = Node(old_node.val)
            old_node = old_node.next

        curr = head

        while curr:
            hash_map[curr].next = hash_map.get(curr.next)
            hash_map[curr].random = hash_map.get(curr.random)
            curr = curr.next

        return hash_map[head]




# Example usage (optional, for testing):
if __name__ == "__main__":
    
    head = [[3,None],[7,3],[4,0],[5,1]]

    # Create the linked list from the input
    nodes = [Node(val) for val, _ in head]
    for i, (val, random_index) in enumerate(head):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    solution = Solution()
    copied_head = solution.copyRandomList(nodes[0])
    # You can add code here to print the copied linked list to verify correctness.
    #print the values of the return head
    current = copied_head
    # output should be like this: Output: [[3,null],[7,3],[4,0],[5,1]]
    output = []
    while current:
        random_index = None
        if current.random:
            random_index = nodes.index(current.random)
        output.append([current.val, random_index])
        current = current.next
    print(output)
