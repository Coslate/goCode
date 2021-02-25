import math

class Solution:
    # @param nums: List[int]
    # @param target: int
    # @return int

    def searchInsertionPosition(self, nums, target):
        return self.__BinarySearch(nums, target);

    def __BinarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = 0

        while(end - start > 1):
            mid = math.floor((start + end)/2)

            if(nums[mid] == target):
                end = mid #find the minimum inserted index
            elif(nums[mid] < target):
                start = mid
            elif(nums[mid] > target):
                end = mid

        if(target < nums[start]):
            ans = start
        elif(target > nums[end]):
            ans = end+1
        else: #nums[start] <= targeet <= nums[end]
            ans = start+1

        print(f'start = {start}')
        print(f'end   = {end}')
        return ans

