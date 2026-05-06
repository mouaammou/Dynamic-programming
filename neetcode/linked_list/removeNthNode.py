from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse and remove and reverse

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr

            curr = temp
        
        i = 1
        curr = prev
        while curr:
            if i + 1 == n:
                curr.next = curr.next.next
                break
            i += 1
            curr = curr.next

        curr = prev
        prev_1 = None
        while curr:
            temp = curr.next
            curr.next = prev_1
            prev_1 = curr

            curr = temp
        
        return prev_1

            



head = [5]
n = 1
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

head = Solution().removeNthFromEnd(list_to_linked_list(head), n) # print all the values
while head:
    print(head.val)
    head = head.next