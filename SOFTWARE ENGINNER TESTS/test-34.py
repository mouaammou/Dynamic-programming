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
# Complete the 'extractAndAppendSponsoredNodes' function below.
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

def extractAndAppendSponsoredNodes(head):
    if not head or not head.next:
        return head

    even_head = even_tail = None
    odd_head = None
    current = head
    index = 1

    while current:
        next_node = current.next  
        
        if index % 2 == 0:

            if not even_head:
                even_head = even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        else:

            current.next = odd_head
            odd_head = current

        current = next_node
        index += 1

    even_tail.next = odd_head

    return even_head

if __name__ == '__main__':

    head = SinglyLinkedList()
    list_items = [10, 20, 30, 40, 50, 60]
    for item in list_items:
        head.insert_node(item)

    result = extractAndAppendSponsoredNodes(head.head)

    print_singly_linked_list(result, '\n')
    print()
