

class SinglyLinkedListNode:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_node(self, node_data):
		node = SinglyLinkedListNode(node_data)

		if not self.head:
			self.head = node
		else:
			self.tail.next = node

		self.tail = node

def print_singly_linked_list(node, sep):
	while node:
		print(node.data, end='')

		node = node.next

		if node:
			print(sep, end='')



#
# Complete the 'removeKthNodeFromEnd' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeKthNodeFromEnd(head, k):
	# Write your code here
	if not head:
		return head
	fast = head
	slow = head
	prev = slow
	while k > 0:
		fast = fast.next
		if not fast:
			return head
		k -= 1

	if not fast.next: #Checks if we are removing head
		return head.next
	while fast.next:
		fast = fast.next
		prev = slow
		slow = slow.next
	prev.next = slow.next
	return head	

if __name__ == '__main__':
	head_count = [1, 2, 3, 4, 5, 6]

	
	head = SinglyLinkedList()
	for num in head_count:
		head.insert_node(num)

	k = 3
	
	result = removeKthNodeFromEnd(head.head, k)

	print_singly_linked_list(result, '\n')
	print()
