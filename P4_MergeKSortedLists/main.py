#! /usr/bin/env python3.6

from MyPackage import solution

#Q.
'''
這道題目曾出現在 Amazon 的面試中。

將 k 個排序過的 linked list merge 成一個新的已排序的 linked list, 並 return merge 後的 linked list head node。Input 是長度為 k 的 array, 該 array 存放 k 個 linked list 的 head node。

時間複雜度要求為 O(nlogk), 其中 n 為 merge 後的 linked list 總長度
Constraints:

k >= 0
Example 1:
Input: lists = [5 -> 10, 1 -> 3 -> 5 -> 7, -1 -> 11, 0 -> 10 -> 20]
Output: -1 -> 0 -> 1 -> 3 -> 5 -> 5 -> 7 -> 10 -> 10 -> 11 -> 20

Example 2:
Input: lists = [-5, -10 -> 100, 9, None]
Output: -10 -> -5 -> 9 -> 100
'''

#########################
#     Main-Routine      #
#########################
def main():

    sol = solution.Solution()
#Example1
    node_5_1  = solution.ListNode(5)
    node_10_1 = solution.ListNode(10)
    node_1    = solution.ListNode(1)
    node_3    = solution.ListNode(3)
    node_5_2  = solution.ListNode(5)
    node_7    = solution.ListNode(7)
    node_n1   = solution.ListNode(-1)
    node_11   = solution.ListNode(11)
    node_0    = solution.ListNode(0)
    node_10_2 = solution.ListNode(10)
    node_20   = solution.ListNode(20)

    node_5_1.next  = node_10_1
    node_1.next    = node_3
    node_3.next    = node_5_2
    node_5_2.next  = node_7
    node_n1.next   = node_11
    node_0.next    = node_10_2
    node_10_2.next = node_20

    head_list = [node_5_1, node_1, node_n1, node_0]
    new_list_head_node = sol.mergeKSortedLists(head_list)
    print(f'Example1 answer: new_list = ', end='')
    solution.printList(new_list_head_node)
    print(f'------------------------------------------------------')

#Example2
    node_n5     = solution.ListNode(-5)
    node_n10    = solution.ListNode(-10)
    node_100   = solution.ListNode(100)
    node_n9     = solution.ListNode(9)

    node_n10.next = node_100
    head_list = [node_n5, node_n10, node_n9, None, None]
    new_list_head_node = sol.mergeKSortedLists(head_list)
    print(f'Example2 answer: new_list = ', end='')
    solution.printList(new_list_head_node)

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
