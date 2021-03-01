#! /usr/bin/env python3.6

from MyPackage import solution

#Q.
'''
這道題目曾出現在 Facebook 的面試中。
給定 Binary Tree 的根節點 root, 找出此 Binary Tree 的最大寬度。

Binary Tree 的寬度定義為: 在某個 tree level 中，最左邊的節點至最右邊的節點的距離
若中間包含空節點 (null node) 則必須將空節點也納入距離的計算
Constraints:

節點值均為整數
最大寬度不會超過 32-bit integer 的可表示範圍
Example:

Input: binary tree =

    Level 0         9 (root)
                   / \
    Level 1       8   7
                 /   / \
    Level 2     6   5   4
                     \
    Level 3           3

Output: 4
Explanation: Level 2 的節點為 [6, null, 5, 4]，其寬度為 4 且是整個 Binary Tree 中最寬的
'''

#########################
#     Main-Routine      #
#########################
def main():
#    input_lev_order = [9, 8, 7, 6, "x", 5, 4, 'x', 'x', 'x', 3, 'x', 'x']
#    bin_tree = solution.BinaryTree()
#    bin_tree.buildBinaryTreeLevelOrder(input_lev_order)
    node_9 = solution.TreeNode(9)
    node_8 = solution.TreeNode(8)
    node_7 = solution.TreeNode(7)
    node_6 = solution.TreeNode(6)
    node_5 = solution.TreeNode(5)
    node_4 = solution.TreeNode(4)
    node_3 = solution.TreeNode(3)

    node_9.left  = node_8
    node_9.right = node_7
    node_8.left  = node_6
    node_7.left  = node_5
    node_7.right = node_4
    node_5.right = node_3

    bin_tree = solution.BinaryTree()
    bin_tree.root = node_9
    bin_tree.traverseNodeLevelOrder()

    sol = solution.Solution()
    max_width = sol.widthOfBinaryTree(bin_tree.root)
    max_width_form = sol.widthOfBinaryTreeFomalAns(bin_tree.root)
    print(f'answer: max_width = {max_width}')
    print(f'formal answer: max_width = {max_width_form}')

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
