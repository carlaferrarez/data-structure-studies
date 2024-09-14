class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if (len(nums) == 1):
            return False
    
        for i in range((len(nums) - 1)):   
            if (nums[i] == nums[i+1]):
                return True
        return False 
# https://neetcode.io/problems/duplicate-integer
# Soluçao time = o (n log n) e space = o (1) 20 min
# Proximo desafio, fazer time = o (n) (hashset)