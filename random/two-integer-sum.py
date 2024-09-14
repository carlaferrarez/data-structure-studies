class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        for j in range(len(nums)):
            for i in range(len(nums)):
                if (nums[j] + nums[i] == target and i != j):
                    return [j, i]
        