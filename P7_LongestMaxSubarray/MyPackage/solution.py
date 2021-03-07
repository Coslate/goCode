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
Output: [3, -1, 3]
Explanation: 
Subarray [3, -1, 3] 的和為 5，長度為 3，是 nums 中擁有最大總和且長度最長的 subarray。
Subarray [5] 也是總和為 5 的 subarray，但長度只有 1。

Example 2:
Input: nums = [-200, 100, -100, 200, -200, 200, -300]
Output: [100, -100, 200, -200, 200]
Explanation: 
Subarray [100, -100, 200, -200, 200] 的和為 200，長度為 5，是 nums 中擁有最大總和且長度最長的 subarray。
Subarray [200] 和 [200, -200, 200] 也是總和為 200 的 subarray，但長度分別只有 1 和 3。
'''
class Solution:

    # @param nums: List[int]
    # @return int
    def longestMaxSubarray(self, nums):
        # Implement me
        prefix    = self.buildPrefix(nums)
        max_i     = 0
        max_j     = 0
        est_j     = 0
        max_len   = -1
        max_sum   = -float("inf")
        min_value = prefix[0]

        for i in range(1, len(nums)):
            new_value = prefix[i] - min_value
            if(new_value > max_sum):
                max_sum = new_value
                max_i = i-1
                max_j = est_j
                max_len = max_i-max_j+1
            elif(new_value == max_sum):
                est_len = i-1-est_j+1
                if(est_len > max_len):
                    max_len = est_len
                    max_i = i-1
                    max_j = est_j

            if(prefix[i] < min_value):
                min_value = prefix[i]
                est_j = i

        print("end_idx = {}, start_idx = {}, max_length = {}".format(max_i, max_j, max_len))
        return max_sum

    def buildPrefix(self, nums):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        return prefix




