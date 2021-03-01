from __future__ import print_function
import sys
import math
import queue
from collections import deque

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def calDistance(in_list):
    start_idx = -1
    end_idx = -1
    for i in range(len(in_list)):
        if(start_idx != -1 and in_list[i] == 1):
            end_idx   = i
        if(start_idx == -1 and in_list[i] == 1):
            start_idx = i
            end_idx   = i

    if(start_idx != -1 and end_idx != -1):
        dist = end_idx - start_idx + 1
    else:
        dist = 0

    print(f'in_list = ', end='')
    [print(f'{x} ', end='') for x in in_list]
    print(f'')
    print(f'start_idx = {start_idx}, end_idx = {end_idx}, dist = {dist}')

    return dist


# Definition of a binary tree node
class TreeNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNodeLevelOrder(self, tree_node):
        #Traverse to find the insertion position
        q = queue.Queue()
        q.put(self.root)

        while(not q.empty()):
            current_node = q.get()
            if(current_node.left == None):
                current_node.left = tree_node
                break
            elif(current_node.right == None):
                current_node.right = tree_node
                break
            else:
                q.put(current_node.left)
                q.put(current_node.right)

    def buildBinaryTreeLevelOrder(self, val_list):
        for val in val_list:
            tree_node = TreeNode(val)
            if(self.root == None):
                self.root = tree_node
            else:
                self.insertNodeLevelOrder(tree_node)

    def traverseNodeLevelOrder(self):
        q = queue.Queue()
        l = queue.Queue()
        q.put(self.root)
        l.put(0)
        level = 0
        last_level = -1

        while(not q.empty()):
            current_node = q.get()
            level        = l.get()
            if(last_level != level):
                print(f'')
                print(f'level = {level}')
                print(f'{current_node.val}', end="")
            else:
                print(f' {current_node.val}', end="")

            if(current_node.left != None):
                q.put(current_node.left)
                l.put(level+1)
            if(current_node.right != None):
                q.put(current_node.right)
                l.put(level+1)

            last_level = level

        print(f"")

#The Binary Tree
class Solution:
    # @param root: TreeNode
    # @return int
    def widthOfBinaryTree(self, root):
        # Implement me
        q = queue.Queue()
        l = queue.Queue()
        q.put(root)
        l.put(0)
        level = 0
        last_level = -1
        width_nxt_list = [1]
        width_listoflist = []
        max_dist = -sys.maxsize

        while(not q.empty()):
            current_node = q.get()
            level        = l.get()
            if(last_level != level):
                width_listoflist.append(width_nxt_list.copy())
                width_nxt_list.clear()

            if(current_node.left != None):
                q.put(current_node.left)
                l.put(level+1)
                width_nxt_list.append(1)
            else:
                width_nxt_list.append(0)
            if(current_node.right != None):
                q.put(current_node.right)
                l.put(level+1)
                width_nxt_list.append(1)
            else:
                width_nxt_list.append(0)

            last_level = level

        for x in range(len(width_listoflist)):
            print(f"")
            print(f'---->level = {x},', end="")
            for y in width_listoflist[x]:
                print(f" {y}", end="")

            print(f'')
            print(f'----->calDistance()...')
            dist_cal = calDistance(width_listoflist[x])
            if(dist_cal > max_dist):
                max_dist = dist_cal

        print(f"")
        return max_dist

    def widthOfBinaryTreeFomalAns(self, root):
        if not root:
            return 0

        # 初始化
        #   - 初始化 Queue，此 Queue 將存放節點以及該節點之編碼
        #   - 初始化最大寬度為 1
        queue = deque()
        queue.append((root, 0)) # (節點, 該節點的編碼)
        maxWidth = 1

        # level-order traversal
        while queue:
            # 計算該層寬度並更新 maxWidth
            minCode, maxCode = queue[0][1], queue[-1][1]
            maxWidth = max(maxWidth, maxCode - minCode + 1)

            # 將下層節點放入 queue
            for _ in range(len(queue)):
                # 從 Queue 中 pop 出目前這層的節點
                node, code = queue.popleft()

                # 將此節點的左子樹及右子樹 push 到 Queue 中
                #   - 左子樹的編碼為當前節點乘以 2
                #   - 右子樹的編碼為當前節點乘以 2 加 1
                if node.left:
                    queue.append((node.left, code * 2 + 0))
                if node.right:
                    queue.append((node.right, code * 2 + 1))

        return maxWidth


