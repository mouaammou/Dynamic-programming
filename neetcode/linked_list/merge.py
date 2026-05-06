from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = node = ListNode(None)


        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        
        node.next = l1 or l2
        return dummy.next

            




        




head = [1, 2, 3, 6]
head2 = [2, 4]
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


head = Solution().mergeTwoLists(list_to_linked_list(head), list_to_linked_list(head2)) # print all the values
while head:
    print(head.val)
    head = head.next