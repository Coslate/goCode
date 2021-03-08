from __future__ import print_function
import sys
import math
import queue
from collections import deque

def printList(nums):
    length = len(nums)

    if(length == 1):
        print(f'[{nums[0]}]')
        return

    for i in range(length):
        if(i == 0):
            print(f"[{nums[i]}", end='')
        elif(i == (length-1)):
            print(f" {nums[i]}]")
        else:
            print(f" {nums[i]}", end='')

# Definition of a binary tree node
class TreeNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # @param root: TreeNode
    # @param k: int
    # @return int
    def findKthSmallestInBST(self, root, k):
        # Implement me
        #In-order traversal
        stack = []
        count = 0
        current_node = root

        while(current_node != None or len(stack) != 0):
            while(current_node != None):
                stack.append(current_node)
                current_node = current_node.left

            count += 1
            top_node = stack[-1]
            stack.pop()
            if(count == k):
                return top_node.val

            current_node = top_node.right

        return None

    def inOrderTraversal(self, root):
        stack = []
        current_node = root

        while(current_node != None or len(stack) != 0):
            while(current_node != None):
                stack.append(current_node)
                current_node = current_node.left

            top_node = stack[-1]
            stack.pop()
            print(" {}".format(top_node.val), end='')

            current_node = top_node.right

        print("")




