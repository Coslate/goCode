#! /usr/bin/env python3.6

from MyPackage import solution

#Q.
'''
這道題目曾出現在 Facebook 的面試中。

給定一個 linked list 的 head node，將指定區間內的節點反轉，並 return 新 linked list 的 head node。

指定區間之定義為: 第 m 個 node 到第 n 個 node 所形成的 linked list
Time complexity 要求: One-pass O(N)
Constraints:

m and n are positive integers
1 <= m < n <= length of the linked list
Example 1:

Input: Linked List = 6 -> 5 -> 4 -> 3 -> 2 -> 1, m = 2, n = 4
Output: 6 -> 3 -> 4 -> 5 -> 2 -> 1
Explanation: 將第二個 node 到第四個 node 所形成的 Linked List 反轉
Example 2:

Input: Linked List = 6 -> 5 -> 4 -> 3 -> 2 -> 1, m = 2, n = 6
Output: 6 -> 1 -> 2 -> 3 -> 4 -> 5
Explanation: 將第二個 node 到第六個 node 所形成的 Linked List 反轉
'''

#########################
#     Main-Routine      #
#########################
def main():
    linked_list_a = solution.SingleLinkedList()
    linked_list_b = solution.SingleLinkedList()
    linked_list_a.insertTail(6)
    linked_list_a.insertTail(5)
    linked_list_a.insertTail(4)
    linked_list_a.insertTail(3)
    linked_list_a.insertTail(2)
    linked_list_a.insertTail(1)

    linked_list_b.insertTail(6)
    linked_list_b.insertTail(5)
    linked_list_b.insertTail(4)
    linked_list_b.insertTail(3)
    linked_list_b.insertTail(2)
    linked_list_b.insertTail(1)

    sol = solution.Solution()
    linked_list_a.head = sol.reverseBetween(linked_list_a.head, 2, 4)
    linked_list_b.head = sol.reverseBetween(linked_list_b.head, 2, 6)
    print(f'linked_list_a = ', end='')
    sol.printList(linked_list_a)
    print(f'linked_list_b = ', end='')
    sol.printList(linked_list_b)

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
