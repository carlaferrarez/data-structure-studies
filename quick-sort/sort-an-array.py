class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## quick sort 
        left = 0
        right = len(nums) - 1

        self.quickSort(nums,left,right)
        return nums

    def quickSort(self,nums,left,right):
        if (left < right):
            pivot = self.partitionArray(nums, left, right)
            self.quickSort(nums,left, pivot - 1)
            self.quickSort(nums,pivot + 1,right)

    def partitionArray(self,nums, left, right):

        pivot = nums[left]
        j = left

        for i in (range(left + 1,right + 1)): ## 1, 4 > 1, 2 e 3
            if pivot >= nums[i]:
                j = j + 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[j], nums[left] = nums[left] , nums[j]
        return j
    
## time litmit exceed
# complexidade de tempo= O(n2)
## complexidade de espaco = O(1)

## https://leetcode.com/problems/sort-an-array/description/