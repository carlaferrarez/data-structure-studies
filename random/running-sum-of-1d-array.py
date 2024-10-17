class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        sum = 0
        for num in nums:
            nums[i] = sum + num
            sum = nums[i]
            i += 1
        return nums
    
# https://leetcode.com/problems/running-sum-of-1d-array/