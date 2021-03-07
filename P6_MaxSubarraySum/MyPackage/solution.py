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
'''
Example 1:
Input: nums = [3, -1, 3, -1, -5, 5, -1, -9]
Output: 5
Explanation: 總和最大的 subarray 包含 [3, -1, 3] 及 [5]，兩者的總和均為 5。

Example 2:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: 總和最大的 subarray 為 [4,-1,2,1]，其總和為 6.
'''
class Solution:

    # @param nums: List[int]
    # @return int
    def maxSubarraySumDP(self, nums):
        # Implement me
        length = len(nums)
        a = [[0] * length for i in range(length)]
        max_sum = -1
        max_i = -1
        max_j = -1

        for i in range(length):
            a[i][i] = nums[i]
            if(max_sum < a[i][i]):
                max_sum = a[i][i]
                max_i = i
                max_j = i
            for j in range(i, -1, -1):
                if(i != j):
                    a[j][i] = a[j][i-1] + a[i][i]
                    if(max_sum < a[j][i]):
                        max_sum = a[j][i]
                        max_i = i
                        max_j = j
        print("max_i = {}, max_j = {}".format(max_i, max_j))
        return max_sum

    def maxSubarraySumPrefix(self, nums):
        # Implement me
        prefix    = self.buildPrefix(nums)
        max_i     = 0
        max_j     = 0
        orig_len  = 0
        max_sum   = -float("inf")
        min_value = prefix[0]

        for i in range(1, len(nums)):
            new_value = prefix[i] - min_value
            if(new_value >= max_sum):
                max_sum = new_value
                max_i = i-1
            if(prefix[i] < min_value):
                min_value = prefix[i]
                max_j = i

        print("max_i = {}, max_j = {}".format(max_i, max_j))
        return max_sum

    def buildPrefix(self, nums):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        return prefix




