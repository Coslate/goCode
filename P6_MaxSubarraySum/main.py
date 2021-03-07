#! /usr/bin/env python3.6

from MyPackage import solution
import argparse

#Q.
'''
這道題目曾出現在 Google 的面試中。

給定一個整數陣列 nums，從中找出總和最大的 subarray，並 return 其總和。
Subarray 為 nums 中連續的元素所組成的 array，其最小長度為 1
Subarray 的總和的定義為該 subarray 中，所有元素的和
時間複雜度要求為 O(n)，其中 n = len(nums)
Constraints:
nums 的長度 >= 1

Example 1:
Input: nums = [3, -1, 3, -1, -5, 5, -1, -9]
Output: 5
Explanation: 總和最大的 subarray 包含 [3, -1, 3] 及 [5]，兩者的總和均為 5。

Example 2:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: 總和最大的 subarray 為 [4,-1,2,1]，其總和為 6.
'''

#########################
#     Main-Routine      #
#########################
def main():
    method = ArgumentParser()
    sol = solution.Solution()
#Example1
    nums = [3, -1, 3, -1, -5, 5, -1, -9]
    print(f'Example1 answer : orig_list = ', end='')
    solution.printList(nums)

    if(method == 1):
        print("> Use DP method...")
        sum_ans = sol.maxSubarraySumDP(nums)
    elif(method == 0):
        print("> Use prefix method...")
        sum_ans = sol.maxSubarraySumPrefix(nums)
    print(f'Example1 answer : {sum_ans}')
    print(f'------------------------------------------------------')
#Example2
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f'Example1 answer : orig_list = ', end='')
    solution.printList(nums)

    if(method == 1):
        print("> Use DP method...")
        sum_ans = sol.maxSubarraySumDP(nums)
    elif(method == 0):
        print("> Use prefix method...")
        sum_ans = sol.maxSubarraySumPrefix(nums)
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
