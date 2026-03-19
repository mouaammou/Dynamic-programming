#!/bin/python3

import math
import os
import random
import re
import sys

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
	first = head
	
	# while head:
	# 	print(head.data)
	# 	head = head.next
	# return 

	while head and head.next:
		while head.next and head.data == head.next.data:
			head.next = head.next.next
		head = head.next
	return first

if __name__ == '__main__':
	head_items = [1, 2, 2, 2]


	head = SinglyLinkedList()

	for i in range(len(head_items)):
		head.insert_node(head_items[i])

	result = deleteDuplicates(head.head)

	print_singly_linked_list(result, '\n')
	print()
