
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
# Complete the 'deleteDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteDuplicates(head):
	current = head
	fast = head
	flag = False
	while current:
		if fast and fast.next and fast.data == fast.next.data:
			flag = True
			fast = fast.next
		elif flag:
			flag = False
			current.next = fast.next
		else:
			current = current.next
			fast = fast.next
	return head

def deleteDuplicates(head):
	current = head
	while current and current.next:
		if current.data == current.next.data:
			current.next = current.next.next
		else:
			current = current.next
	return head

if __name__ == '__main__':
	head_count = [2, 2, 2, 2, 2]

	head = SinglyLinkedList()

	for num in head_count:
		head.insert_node(num)

	result = deleteDuplicates(head.head)

	print_singly_linked_list(result, '\n')
	print()