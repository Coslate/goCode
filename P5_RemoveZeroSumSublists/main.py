#! /usr/bin/env python3.6

from MyPackage import solution

#Q.
'''
這道題目曾出現在 Uber 的面試中。

給定一個 linked list 的 head node, 刪除所有總和為 0 的 sub linked lists, 直到此 linked list 不存在一個總和為 0 的 sub linked list 為止, 最後 return 刪除後的 linked list head node。

Example 1:
Input: 3 -> 2 -> 1 -> -1 -> -2 -> None
Output: 3 -> None
Explanation: Sub list 2 -> 1 -> -1 -> -2 的總和為 0, 所以可把此 sub list 刪除

Example 2:
Input: -5 -> 2 -> 1 -> -3 -> 10 -> 1 -> 2 -> -2 -> None
Output -5 -> 10 -> 1 -> None
Explanation: Sub lists 2 -> 1 -> -3 及 2 -> -2 各自的總和為 0, 所以可把這兩個 sub lists 刪除
'''

#########################
#     Main-Routine      #
#########################
def main():
    sol = solution.Solution()
#Example1
    node_3  = solution.ListNode(3)
    node_2  = solution.ListNode(2)
    node_1  = solution.ListNode(1)
    node_n1 = solution.ListNode(-1)
    node_n2 = solution.ListNode(-2)

    node_3.next  = node_2
    node_2.next  = node_1
    node_1.next  = node_n1
    node_n1.next = node_n2

    print(f'Example1 answer : orig_list = ', end='')
    solution.printList(node_3)

    new_list_head_node = sol.removeZeroSumSublists(node_3)
    print(f'Example1 answer : new_list  = ', end='')
    solution.printList(new_list_head_node)
    print(f'------------------------------------------------------')

    node_n5   = solution.ListNode(-5)
    node_2    = solution.ListNode(2)
    node_1    = solution.ListNode(1)
    node_n3   = solution.ListNode(-3)
    node_10   = solution.ListNode(10)
    node_1_2  = solution.ListNode(1)
    node_2_2  = solution.ListNode(2)
    node_n2   = solution.ListNode(-2)

    node_n5.next = node_2
    node_2.next = node_1
    node_1.next = node_n3
    node_n3.next = node_10
    node_10.next = node_1_2
    node_1_2.next = node_2_2
    node_2_2.next = node_n2

    print(f'Example2 answer : orig_list = ', end='')
    solution.printList(node_n5)

    new_list_head_node = sol.removeZeroSumSublists(node_n5)
    print(f'Example2 answer : new_list  = ', end='')
    solution.printList(new_list_head_node)

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
