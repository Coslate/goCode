from __future__ import print_function
import sys
import math
import queue
from collections import deque

def printList(head):
    current_node = head
    while(current_node != None):
        val = current_node.val
        if(current_node == head):
            print(f"[{val}", end='')
        elif(current_node.next == None):
            print(f" {val}]")
        else:
            print(f" {val}", end='')

        current_node = current_node.next

# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def merge2SortedLists(self, head_node1, head_node2):
        if(head_node1 == None):
            return head_node2
        if(head_node2 == None):
            return head_node1

        current_node1 = head_node1
        current_node2 = head_node2
        new_list_head = None
        current_node  = None
        while(current_node1 != None and current_node2 != None):
            if(current_node1.val < current_node2.val):
                if(new_list_head == None):
                    new_list_head = current_node1
                    current_node = new_list_head
                else:
                    current_node.next = current_node1
                    current_node = current_node.next
                current_node1 = current_node1.next
            else:
                if(new_list_head == None):
                    new_list_head = current_node2
                    current_node = new_list_head
                else:
                    current_node.next = current_node2
                    current_node = current_node.next
                current_node2 = current_node2.next

        if(current_node1 == None and current_node2 != None):
            current_node.next = current_node2
        elif(current_node1 != None and current_node2 == None):
            current_node.next = current_node1

        return new_list_head

    # @param lists: List[ListNode]
    # @return ListNode
    def mergeKSortedLists(self, lists):
        # Implement me
        len_of_lists = len(lists)
        while(len_of_lists > 1):
            if(len_of_lists %2 == 0):#even
                for i in range(int(len_of_lists/2)):
                    lists[i] = self.merge2SortedLists(lists[i], lists[-1])
                    lists.pop()
            else:#odd
                for i in range(int((len_of_lists-1)/2)):
                    lists[i] = self.merge2SortedLists(lists[i], lists[-1])
                    lists.pop()

            len_of_lists = len(lists)
        return lists[0]


