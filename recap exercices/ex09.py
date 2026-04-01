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
	dummy = SinglyLinkedListNode(0)
	dummy.next = head
	fast = slow = dummy

	for i in range(k + 2):
		print(i)
		if fast is None:
			return head # means K is not valid
		fast = fast.next
	
	while fast:
		fast = fast.next
		slow = slow.next

	slow.next = slow.next.next
	return dummy.next

if __name__ == '__main__':
	head_items = [5, 6, 7, 8]
	head = SinglyLinkedList()

	for i in range(len(head_items)):
		head.insert_node(head_items[i])

	k = 3

	result = removeKthNodeFromEnd(head.head, k)

	# print_singly_linked_list(result, '\n')
	# print()
