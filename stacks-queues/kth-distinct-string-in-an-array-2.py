class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        if (k > len(arr)):
            return ""
        stack=[]
        
        for i in arr:
            count_number = arr.count(i)
            if (count_number == 1):
                stack.append(i)
        if (k <= len(stack)):
            return stack[k - 1]
        else:
            return ""
                
# complexidade de espaço: O(n)
# complexidade de tempo: O(n)2
# https://leetcode.com/problems/kth-distinct-string-in-an-array/