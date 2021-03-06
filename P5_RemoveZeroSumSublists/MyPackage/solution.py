from __future__ import print_function
import sys
import math
import queue
from collections import deque

def printList(head):
    current_node = head
    while(current_node != None):
        val = current_node.val
        if(current_node == head and current_node.next == None):
            print(f"[{val}]")
        elif(current_node == head):
            print(f"[{val}", end='')
        elif(current_node.next == None):
            print(f" {val}]")
        else:
            print(f" {val}", end='')

        current_node = current_node.next

def searchPosition(list_elem, pos):
    current_val = list_elem[pos]
    current_pos = pos-1
    ans_pos = -1
    sum_elem = list_elem[current_pos] + current_val

    while(current_pos >= 0):
        if(sum_elem == 0):
            ans_pos = current_pos
            break

        current_pos = current_pos - 1
        sum_elem = sum_elem + list_elem[current_pos]
    return ans_pos

def deleteSublist(head, start_pos, end_pos, list_size):
    if(end_pos - start_pos + 1 == list_size):
        return None

    new_head = head
    start_node = None
    end_node   = None
    current_node = head
    current_pos = 0
    while(current_node != None):
        if(current_pos == start_pos - 1):
            start_node = current_node
        if(current_pos == end_pos):
            end_node = current_node
        current_node = current_node.next
        current_pos = current_pos + 1

    if(start_pos == 0 and end_node != None):
        new_head = end_node.next
        end_node.next = None
    else:
        if(start_node != None and end_node != None):
            print("start_node = {}, end_node = {}, start_pos = {}, end_pos = {}".format(start_node.val, end_node.val, start_pos, end_pos))
            start_node.next = end_node.next
            end_node.next   = None
        elif(start_node != None and end_node == None):
            print("start_node = {}, start_pos = {}, end_pos = {}".format(start_node.val, start_pos, end_pos))
            start_node.next = None

    return new_head

def buildArray(head, list_elem):
    list_size = 0
    current_node = head
    while(current_node != None):
        list_elem.append(current_node.val)
        current_node = current_node.next
        list_size = list_size + 1
    return list_size

# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param head: ListNode
    # @retrun ListNode
    def removeZeroSumSublistsNaive(self, head):
        # Implement me
        ans_pos = -1
        new_head = head
        list_elem = []
        list_size = buildArray(head, list_elem)

        current_node = head
        curr_pos = 0
        while(current_node != None):
            ans_pos = searchPosition(list_elem, curr_pos)
            print("current_node = {}, ans_pos = {}, curr_pos = {}".format(current_node.val, ans_pos, curr_pos))
            current_node_next = current_node.next
            if(ans_pos != -1):
                new_head = deleteSublist(new_head, ans_pos, curr_pos, list_size)
                list_elem = []
                list_size = buildArray(head, list_elem)
                curr_pos = curr_pos - (curr_pos - ans_pos + 1)

            current_node = current_node_next
            curr_pos = curr_pos + 1

        return new_head

    def removeZeroSumSublistsTable(self, head):
        table = {}
        dummy_node = ListNode(0)
        dummy_node.next = head
        self.buildTable(table, dummy_node)

        current_node = dummy_node
        current_sum  = 0
        while(current_node):
            current_sum  = current_sum + current_node.val
            current_node.next = table[current_sum].next
            current_node = current_node.next

        return dummy_node.next

    def buildTable(self, table, head):
        current_node = head
        sum_to_node = 0
        while(current_node):
            sum_to_node = sum_to_node + current_node.val
            table[sum_to_node] = current_node
            current_node = current_node.next




