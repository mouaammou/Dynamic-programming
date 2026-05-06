from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast.next:
            print(fast.val)
            fast = fast.next.next



head = [1, 2]
# Convert the list to a linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

head = Solution().hasCycle(list_to_linked_list(head)) # print all the values
while head:
    print(head.val)
    head = head.next