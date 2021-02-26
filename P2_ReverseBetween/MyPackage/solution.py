from __future__ import print_function
import sys
import math

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class ListNode:
    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, val):
        new_node = ListNode(val)

        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node

class Solution:

    # @param head: ListNode
    # @param m: int
    # @param n: int
    # @return ListNode
    def reverseBetween(self, head, m, n):
        # Implement me
        if(head == None):
            print(f'Error: head is None')
            return None

        if(m > n):
            print(f'Error: m > n')
            return None

        tmp_list       = []
        start_pre_node = None
        start_rev_node = None
        end_rev_node   = None
        end_nxt_node   = None
        current_node   = head
        count = 0

        while(current_node != None):
            count = count+1
            if((count >= m) and (count <= n)):
                if(count == m):
                    start_rev_node = current_node
                elif(count == n):
                    end_rev_node = current_node

                tmp_list.append(current_node)

            if(count+1==m):
                start_pre_node = current_node
            if(count-1==n):
                end_nxt_node   = current_node
            current_node = current_node.next

        if(start_pre_node == None):
            head = tmp_list[-1]
        else:
            start_pre_node.next = tmp_list[-1]

        if(end_nxt_node == None):
            tail = tmp_list[0]
            tmp_list[0].next = None
        else:
            tmp_list[0].next = end_nxt_node

        i = len(tmp_list)-1
        while(i >= 0):
            if(i > 0):
                tmp_list[i].next = tmp_list[i-1]
            i=i-1

        return head

    def printList(self, linked_list):
        current_node = linked_list.head
        while(current_node != None):
            if(current_node.next == None):
                print(f'{current_node.val}')
            else:
                print(f'{current_node.val} -> ', end='')

            current_node = current_node.next

