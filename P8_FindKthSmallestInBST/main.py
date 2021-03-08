#! /usr/bin/env python3.6

from MyPackage import solution
import argparse

#Q.
'''
這道題目曾出現在 Amazon 的面試中。

給定 Binary Search Tree (BST) 的根節點 root, 找出在此 BST 中第 k 小的數.
時間複雜度要求為 O(n)
Constraints:
此 BST 至少存在一個 node
1 <= k <= number of total nodes in the BST

Example:

Input: k = 4, binary tree =

    Level 0         5 (root)
                   / \
    Level 1       3   9
                 /   / \
    Level 2    -1   6   10
                     \
    Level 3           7

Output: 6
Explanation: 此 BST 的 node 由小至大排序為 [-1, 3, 5, 6, 7, 9, 10]，所以第 4 小的 node 為 6

'''

#########################
#     Main-Routine      #
#########################
def main():
    method = ArgumentParser()
    sol = solution.Solution()
#Example1
    node_5  = solution.TreeNode(5)
    node_3  = solution.TreeNode(3)
    node_9  = solution.TreeNode(9)
    node_n1 = solution.TreeNode(-1)
    node_6  = solution.TreeNode(6)
    node_10 = solution.TreeNode(10)
    node_7  = solution.TreeNode(7)

    node_5.left  = node_3
    node_5.right = node_9
    node_3.left  = node_n1
    node_9.left  = node_6
    node_9.right = node_10
    node_6.right = node_7

    print("Original Tree:", end = "")
    sol.inOrderTraversal(node_5)
    sum_ans = sol.findKthSmallestInBST(node_5, 4)
    print(f'Example1 answer : {sum_ans}')
    print(f'------------------------------------------------------')

#########################
#     Sub-Routine       #
#########################
def ArgumentParser():
    method                 = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--method", "-method", help="1: Use DP method, O(n^2). 0: Use prefix method, O(n). Default is 0.")

    args = parser.parse_args()
    if args.method:
        method = int(args.method)

    return method

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
