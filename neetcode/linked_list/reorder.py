from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     nodes = []

    #     curr = head
    #     while curr:
    #         nodes.append(curr)
    #         curr = curr.next
        

    #     i = 0
    #     j = len(nodes) - 1

    #     while i < j:
    #         nodes[i].next = nodes[j]
    #         i += 1
    #         # if i >= j:
    #         #     break
    #         nodes[j].next = nodes[i]
    #         j -= 1
    #     nodes[i].next = None


    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        seconde = slow.next
        prev = None
        while seconde:
            temp = seconde.next
            seconde.next = prev
            prev = seconde

            seconde = temp

        

head = [1, 2, 3, 4, 5]

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

linked_head = list_to_linked_list(head)
Solution().reorderList(linked_head)

current = linked_head
while current:
    print(current.val)
    current = current.next